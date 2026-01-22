# Day-Based Collector Auto-Assignment (Smart Rotation)

**Feature:** Auto-assign collectors to farmer waste orders using day-based rotation  
**Date:** 2026-01-22

---

## Concept: Smart Day-Based Rotation

### **How It Works:**

**Monday** → Collector A gets orders  
**Tuesday** → Collector B gets orders  
**Wednesday** → Collector C gets orders  
**Thursday** → Collector A gets orders (rotation repeats)  
...and so on

**BUT** - if the assigned collector doesn't have enough stock, **automatically switch to the next available collector**.

---

## Implementation Logic

### **Step 1: Determine Today's Collector**

```python
def get_todays_collector():
    """
    Assign collectors based on day of week rotation.
    Returns the collector assigned for today.
    """
    from datetime import datetime

    # Get all verified collectors
    collectors = Collector.objects.filter(
        user__is_verified=True
    ).order_by('id')  # Consistent ordering

    if not collectors.exists():
        return None

    # Get day of week (0=Monday, 6=Sunday)
    day_of_week = datetime.now().weekday()

    # Rotate through collectors based on day
    collector_index = day_of_week % collectors.count()

    return collectors[collector_index]
```

**Example with 3 collectors:**

- Monday (0): Collector A (index 0)
- Tuesday (1): Collector B (index 1)
- Wednesday (2): Collector C (index 2)
- Thursday (3): Collector A (3 % 3 = 0)
- Friday (4): Collector B (4 % 3 = 1)
- Saturday (5): Collector C (5 % 3 = 2)
- Sunday (6): Collector A (6 % 3 = 0)

---

### **Step 2: Check Stock & Auto-Switch**

```python
def auto_assign_collector_to_farmer_order(order_id):
    """
    Auto-assign collector to farmer waste order using day-based rotation.
    If today's collector doesn't have enough stock, switch to next available.

    Returns: (Collector, assignment_type)
    - assignment_type: 'rotation' or 'fallback'
    """
    from django.db.models import Sum, Q

    order = tbl_Order.objects.get(pk=order_id)
    required_qty = order.total_quantity

    # Get all verified collectors
    all_collectors = list(Collector.objects.filter(
        user__is_verified=True
    ).order_by('id'))

    if not all_collectors:
        return None, 'no_collectors'

    # Step 1: Get today's assigned collector (rotation)
    todays_collector = get_todays_collector()

    # Step 2: Check if today's collector has enough stock
    available_stock = tbl_WasteInventory.objects.filter(
        collector=todays_collector,
        status='Available'
    ).aggregate(
        total=Sum('available_quantity_kg')
    )['total'] or 0

    if available_stock >= required_qty:
        # Perfect! Today's collector can fulfill the order
        return todays_collector, 'rotation'

    # Step 3: Today's collector doesn't have enough - find next available
    # Start from today's collector and check each one in rotation
    start_index = all_collectors.index(todays_collector)

    for i in range(1, len(all_collectors)):
        # Get next collector in rotation
        next_index = (start_index + i) % len(all_collectors)
        next_collector = all_collectors[next_index]

        # Check their stock
        available_stock = tbl_WasteInventory.objects.filter(
            collector=next_collector,
            status='Available'
        ).aggregate(
            total=Sum('available_quantity_kg')
        )['total'] or 0

        if available_stock >= required_qty:
            # Found a collector with enough stock!
            return next_collector, 'fallback'

    # No collector has enough stock
    return None, 'insufficient_stock'
```

---

## Example Scenarios

### **Scenario 1: Normal Rotation (Success)**

- **Day:** Monday
- **Today's Collector:** Collector A
- **Order:** 100kg waste
- **Collector A's Stock:** 150kg ✅
- **Result:** ✅ Assigned to **Collector A** (rotation)

---

### **Scenario 2: Auto-Switch (Fallback)**

- **Day:** Tuesday
- **Today's Collector:** Collector B
- **Order:** 100kg waste
- **Collector B's Stock:** 50kg ❌ Not enough
- **Next in rotation:** Collector C
- **Collector C's Stock:** 120kg ✅
- **Result:** ✅ Assigned to **Collector C** (fallback)

---

### **Scenario 3: Multiple Switches**

- **Day:** Wednesday
- **Today's Collector:** Collector C
- **Order:** 200kg waste
- **Collector C's Stock:** 80kg ❌
- **Collector A's Stock:** 100kg ❌
- **Collector B's Stock:** 250kg ✅
- **Result:** ✅ Assigned to **Collector B** (fallback after 2 checks)

---

### **Scenario 4: No One Has Stock**

- **Day:** Thursday
- **Order:** 300kg waste
- **All Collectors:** < 300kg each
- **Result:** ❌ **Manual assignment required** (notify admin)

---

## Benefits of Day-Based Rotation

✅ **Fair Distribution:** Each collector gets equal opportunity  
✅ **Predictable:** Collectors know their assigned days  
✅ **Simple:** Easy to understand and explain  
✅ **Automatic Fallback:** Switches if stock is insufficient  
✅ **No Manual Work:** Fully automated  
✅ **Balanced Workload:** Evenly distributes orders over time

---

## Admin Dashboard View

### **Assignment Summary:**

```
Today's Assigned Collector: Collector A (Monday)

Recent Auto-Assignments:
┌──────────┬────────────┬──────────────┬─────────────┬──────────────┐
│ Order ID │ Date       │ Assigned To  │ Type        │ Reason       │
├──────────┼────────────┼──────────────┼─────────────┼──────────────┤
│ #1234    │ 2026-01-22 │ Collector A  │ Rotation    │ Monday       │
│ #1235    │ 2026-01-22 │ Collector C  │ Fallback    │ A had 50kg   │
│ #1236    │ 2026-01-22 │ Collector A  │ Rotation    │ Monday       │
│ #1237    │ 2026-01-21 │ Collector C  │ Rotation    │ Sunday       │
└──────────┴────────────┴──────────────┴─────────────┴──────────────┘
```

---

## Enhanced Version: Weekly Schedule

For more control, you can assign specific days to specific collectors:

```python
# In SystemSettings or new model
COLLECTOR_SCHEDULE = {
    'Monday': 'Collector A',
    'Tuesday': 'Collector B',
    'Wednesday': 'Collector C',
    'Thursday': 'Collector A',
    'Friday': 'Collector B',
    'Saturday': 'Collector C',
    'Sunday': 'Collector A'
}
```

Admin can customize this schedule from the dashboard.

---

## Database Changes (Optional)

### **Track Assignment History:**

```python
class tbl_CollectorAssignmentLog(models.Model):
    """Track auto-assignment decisions for transparency"""
    order = models.ForeignKey(tbl_Order, on_delete=models.CASCADE)
    assigned_collector = models.ForeignKey(Collector, on_delete=models.CASCADE)
    assignment_type = models.CharField(max_length=20)  # 'rotation' or 'fallback'
    todays_collector = models.ForeignKey(Collector, related_name='scheduled_for')
    reason = models.TextField()  # "Monday rotation" or "Fallback: A had 50kg, needed 100kg"
    assigned_at = models.DateTimeField(auto_now_add=True)
```

---

## Complete Implementation

```python
# In MyApp/sales_views.py

@login_required(login_url='login')
@never_cache
def auto_assign_farmer_order(request, order_id):
    """
    Auto-assign collector to farmer waste order using day-based rotation.
    """
    if request.method == 'POST':
        order = tbl_Order.objects.get(pk=order_id)

        # Check if already assigned
        if order.assigned_collector:
            return JsonResponse({
                'success': False,
                'error': 'Order already has an assigned collector'
            })

        # Auto-assign using rotation
        collector, assignment_type = auto_assign_collector_to_farmer_order(order_id)

        if collector:
            # Create FarmerSupply record
            tbl_FarmerSupply.objects.create(
                Order_id=order,
                Collection_id=None,  # Will be updated when collector delivers
                Collector_id=collector,
                Quantity_kg=order.total_quantity,
                Price_per_kg=10.00,  # From system settings
                Supply_date=None,  # Will be set on delivery
                status='Pending'
            )

            # Update order
            order.assigned_collector = collector
            order.save()

            # Log the assignment (optional)
            day_name = datetime.now().strftime('%A')
            reason = f"{day_name} rotation" if assignment_type == 'rotation' else f"Fallback (insufficient stock)"

            messages.success(
                request,
                f'✅ Order #{order.Order_id} auto-assigned to {collector.collector_name} ({reason})'
            )

            return JsonResponse({
                'success': True,
                'collector_name': collector.collector_name,
                'assignment_type': assignment_type,
                'message': f'Assigned to {collector.collector_name}'
            })
        else:
            # No collector available
            messages.error(
                request,
                '❌ No collector has sufficient stock. Manual assignment required.'
            )
            return JsonResponse({
                'success': False,
                'error': 'No collector has sufficient stock',
                'required_qty': order.total_quantity
            })

    return JsonResponse({'success': False, 'error': 'Invalid request'})
```

---

## UI Changes

### **Add "Auto-Assign" Button:**

```html
<!-- In templates/Admin/waste_sales.html -->
<button
  onclick="autoAssignOrder({{ order.Order_id }})"
  class="btn btn-success btn-sm"
>
  🤖 Auto-Assign (Today: {{ todays_collector_name }})
</button>

<script>
  function autoAssignOrder(orderId) {
    if (confirm("Auto-assign collector based on today's rotation?")) {
      fetch(`/admin/auto-assign-order/${orderId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": "{{ csrf_token }}",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            Swal.fire("Success!", data.message, "success").then(() =>
              location.reload(),
            );
          } else {
            Swal.fire("Error", data.error, "error");
          }
        });
    }
  }
</script>
```

---

## Summary

**Day-Based Rotation System:**

1. ✅ Each day has an assigned collector (rotation)
2. ✅ System checks if they have enough stock
3. ✅ If not, automatically switches to next collector
4. ✅ Keeps trying until finds one with stock
5. ✅ If none have stock, notifies admin for manual assignment

**This is simpler, fairer, and more predictable than inventory-based assignment!**

Ready to implement this? It's about 2-3 hours of work!
