# Auto-Assignment Logic for Collector Assignment

**Feature:** Automated Collector Assignment for Farmer Waste Orders  
**Date:** 2026-01-22

---

## Assignment Criteria (Priority Order)

When a farmer places a waste order, the system will auto-assign a collector based on these criteria:

### **1. Inventory Availability** (Primary Criterion) ⭐

**Logic:** Assign the collector who has the **most available inventory** that matches the order requirements.

**Why:**

- Ensures the collector can fulfill the order
- Prevents assigning collectors with insufficient stock
- Balances workload across collectors

**Implementation:**

```python
# Find collectors with available inventory >= order quantity
collectors_with_stock = Collector.objects.annotate(
    available_qty=Sum(
        'wasteinventory__quantity_kg',
        filter=Q(wasteinventory__status='Available')
    )
).filter(
    available_qty__gte=order.total_quantity
).order_by('-available_qty')
```

---

### **2. Waste Type Match** (Secondary Criterion)

**Logic:** Prioritize collectors who have the **exact waste type** the farmer ordered.

**Why:**

- Ensures quality match
- Faster fulfillment
- Better customer satisfaction

**Implementation:**

```python
# Filter by waste type if farmer ordered specific type
if order.waste_type:
    collectors_with_stock = collectors_with_stock.filter(
        wasteinventory__waste_type=order.waste_type,
        wasteinventory__status='Available'
    )
```

---

### **3. Freshness of Waste** (Tertiary Criterion)

**Logic:** Prefer collectors with **newer waste** (recently collected).

**Why:**

- Better quality for farmers
- Reduces risk of expiry
- Encourages faster turnover

**Implementation:**

```python
# Prefer collectors with most recent collections
collectors_with_stock = collectors_with_stock.annotate(
    avg_collection_age=Avg(
        ExpressionWrapper(
            Now() - F('wasteinventory__collection_date'),
            output_field=DurationField()
        )
    )
).order_by('avg_collection_age')  # Newest first
```

---

### **4. Collector Performance** (Future Enhancement)

**Logic:** Prioritize collectors with **higher ratings** and **better delivery records**.

**Why:**

- Rewards good performance
- Ensures quality service
- Encourages collector excellence

**Implementation (Future):**

```python
# When rating system is implemented
collectors_with_stock = collectors_with_stock.annotate(
    avg_rating=Avg('collectionrequest__rating')
).filter(
    avg_rating__gte=3.5  # Minimum 3.5 stars
).order_by('-avg_rating')
```

---

### **5. Geographic Proximity** (Future Enhancement)

**Logic:** Assign collectors **closest to the farmer** to reduce delivery time and cost.

**Why:**

- Faster delivery
- Lower fuel costs
- Better sustainability

**Implementation (Future - requires GPS):**

```python
# When GPS coordinates are available
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

farmer_location = Point(farmer.longitude, farmer.latitude)
collectors_with_stock = collectors_with_stock.annotate(
    distance=Distance('location', farmer_location)
).order_by('distance')  # Closest first
```

---

## Complete Auto-Assignment Algorithm

### **Current Implementation (Phase 1)**

```python
def auto_assign_collector_to_order(order_id):
    """
    Automatically assign the best collector to a farmer's waste order.

    Assignment Priority:
    1. Has sufficient available inventory
    2. Has matching waste type (if specified)
    3. Has freshest waste (newest collection date)
    4. Is verified/active

    Returns: Collector object or None if no suitable collector found
    """
    from django.db.models import Sum, Avg, F, Q, ExpressionWrapper, DurationField
    from django.utils.timezone import now

    order = tbl_Order.objects.get(pk=order_id)

    # Step 1: Find collectors with sufficient available inventory
    collectors = Collector.objects.filter(
        user__is_verified=True  # Only verified collectors
    ).annotate(
        available_qty=Sum(
            'wasteinventory__quantity_kg',
            filter=Q(wasteinventory__status='Available')
        )
    ).filter(
        available_qty__gte=order.total_quantity  # Has enough stock
    )

    # Step 2: Filter by waste type if order specifies one
    # (Assuming order has waste_type field - may need to add)
    # if hasattr(order, 'waste_type') and order.waste_type:
    #     collectors = collectors.filter(
    #         wasteinventory__waste_type=order.waste_type,
    #         wasteinventory__status='Available'
    #     ).distinct()

    # Step 3: Prioritize by freshness (newest waste first)
    collectors = collectors.annotate(
        newest_collection=Max('wasteinventory__collection_date')
    ).order_by('-newest_collection', '-available_qty')

    # Return the best match
    return collectors.first()
```

---

## Assignment Logic Summary

### **Ranking System:**

| Criterion                  | Weight      | Description                     |
| -------------------------- | ----------- | ------------------------------- |
| **Inventory Availability** | 🔴 Critical | Must have >= order quantity     |
| **Waste Type Match**       | 🟡 High     | Prefer exact match if specified |
| **Waste Freshness**        | 🟡 High     | Prefer newest collections       |
| **Collector Status**       | 🔴 Critical | Must be verified/active         |
| **Performance Rating**     | 🟢 Future   | Prefer higher-rated collectors  |
| **Geographic Proximity**   | 🟢 Future   | Prefer closest collectors       |

---

## Example Scenarios

### **Scenario 1: Simple Assignment**

- **Order:** 100kg waste, no specific type
- **Available Collectors:**
  - Collector A: 150kg available (collected 2 days ago)
  - Collector B: 120kg available (collected 5 days ago)
  - Collector C: 80kg available (collected 1 day ago)
- **Result:** ✅ **Collector A** (most stock + fresh)

---

### **Scenario 2: Freshness Priority**

- **Order:** 50kg waste
- **Available Collectors:**
  - Collector A: 200kg available (collected 10 days ago)
  - Collector B: 60kg available (collected 1 day ago)
  - Collector C: 100kg available (collected 5 days ago)
- **Result:** ✅ **Collector B** (freshest waste, sufficient stock)

---

### **Scenario 3: No Suitable Collector**

- **Order:** 200kg waste
- **Available Collectors:**
  - Collector A: 50kg available
  - Collector B: 100kg available
  - Collector C: 80kg available
- **Result:** ❌ **None** (manual assignment required, notify admin)

---

## Fallback Mechanism

If auto-assignment fails (no suitable collector found):

1. **Notify Admin** via dashboard alert
2. **Email Admin** with order details
3. **Show "Manual Assignment Required"** badge on order
4. **Suggest Alternatives:**
   - Wait for more inventory
   - Split order across multiple collectors
   - Contact collectors to request more collections

---

## Benefits of This Approach

✅ **Fair Distribution:** Balances workload across collectors  
✅ **Quality Assurance:** Prioritizes fresh waste  
✅ **Efficiency:** Instant assignment, no manual work  
✅ **Transparency:** Clear criteria, auditable decisions  
✅ **Scalability:** Works with any number of collectors  
✅ **Flexibility:** Easy to adjust priorities

---

## Future Enhancements

### **Phase 2 (Advanced):**

1. **Machine Learning:** Learn from past successful assignments
2. **Predictive Analytics:** Forecast inventory availability
3. **Dynamic Pricing:** Adjust prices based on demand/supply
4. **Multi-Collector Orders:** Split large orders automatically
5. **Delivery Time Estimation:** Show expected delivery time
6. **Collector Preferences:** Allow collectors to set availability

---

## Implementation Notes

### **Database Changes Needed:**

- ✅ No changes required (uses existing fields)
- 🟡 Optional: Add `waste_type` to `tbl_Order` for better matching
- 🟡 Optional: Add `rating` to `tbl_CollectionRequest` for performance tracking

### **Code Changes:**

- Create `auto_assign_collector_to_order()` in `MyApp/sales_views.py`
- Add "Auto-Assign" button in `templates/Admin/waste_sales.html`
- Add AJAX handler for auto-assignment
- Add success/failure notifications

### **Testing Checklist:**

- [ ] Test with sufficient inventory
- [ ] Test with insufficient inventory
- [ ] Test with no collectors
- [ ] Test with multiple suitable collectors
- [ ] Test with expired waste
- [ ] Test with unverified collectors

---

## Conclusion

The auto-assignment algorithm uses a **smart, multi-criteria approach** that prioritizes:

1. **Availability** (can they fulfill the order?)
2. **Quality** (is the waste fresh?)
3. **Fairness** (balanced workload)

This ensures **optimal assignments** while maintaining **flexibility** for future enhancements like ratings and GPS-based proximity.

**Ready to implement?** This can be added in ~2-3 hours of development time!
