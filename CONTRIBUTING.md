# Contributing to BioBinConnect

Thank you for your interest in contributing to BioBinConnect! 🌱

## How to Contribute

### 1. Fork the Repository

Fork the project on GitHub and clone your fork locally.

```bash
git clone https://github.com/yourusername/BioBinConnect.git
cd BioBinConnect/MyProject
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env with your local settings

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation if needed

### 5. Test Your Changes

```bash
python manage.py test
```

### 6. Commit Your Changes

```bash
git add .
git commit -m "Add: Brief description of your changes"
```

**Commit Message Format:**

- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for updates to existing features
- `Docs:` for documentation changes
- `Refactor:` for code refactoring

### 7. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Code Style Guidelines

### Python

- Follow PEP 8
- Use meaningful variable names
- Maximum line length: 100 characters
- Use docstrings for functions and classes

### Django

- Use Django best practices
- Keep views simple, move logic to models/utils
- Use Django ORM instead of raw SQL
- Follow Django naming conventions

### Templates

- Use semantic HTML5
- Keep templates DRY (Don't Repeat Yourself)
- Use template inheritance
- Add comments for complex sections

### JavaScript

- Use vanilla JavaScript (no jQuery)
- Use meaningful function names
- Add comments for complex logic

## What to Contribute

### Bug Fixes

- Check existing issues first
- Create an issue if one doesn't exist
- Reference the issue in your PR

### New Features

- Discuss major features in an issue first
- Ensure features align with project goals
- Update documentation

### Documentation

- Fix typos and errors
- Improve clarity
- Add examples
- Update README if needed

### Tests

- Add tests for new features
- Improve test coverage
- Fix failing tests

## Pull Request Process

1. Update README.md with details of changes if needed
2. Update documentation
3. Ensure all tests pass
4. Request review from maintainers
5. Address review feedback
6. Wait for approval and merge

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Publishing private information
- Unprofessional conduct

## Questions?

Feel free to:

- Open an issue for questions
- Email: contact@biobinconnect.com
- Join discussions in pull requests

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making BioBinConnect better! 🌱**
