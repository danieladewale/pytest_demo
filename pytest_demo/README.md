# GitHub Actions Tutorial: Automated Testing with Python

Welcome! This repository is designed to help you learn **GitHub Actions** - a powerful CI/CD (Continuous Integration/Continuous Deployment) tool that automates tasks in your software development workflow.

## 📚 What You'll Learn

By the end of this tutorial, you will understand:
- What GitHub Actions is and why it's useful
- How to read and understand a GitHub Actions workflow file
- How to set up automated testing for Python projects
- How to trigger workflows and interpret results
- How to modify workflows for your own projects

---

## 🎯 What is GitHub Actions?

**GitHub Actions** is a platform that lets you automate software development workflows directly in your GitHub repository. Think of it as a robot that:
- Runs automatically when you push code or create pull requests
- Tests your code to make sure it works
- Can deploy your application
- Can run on different operating systems and Python versions

**Why use it?** Instead of manually running tests every time you write code, GitHub Actions does it automatically and tells you if something breaks!

---

## 📁 Project Overview

This project contains a simple calculator with automated tests. Here's what's in the repository:

```
.
├── calculator.py          # Simple calculator module (the code we're testing)
├── test_calculator.py     # Unit tests using pytest (tests for the calculator)
├── requirements.txt       # Python dependencies (pytest, pytest-cov)
├── .github/
│   └── workflows/
│       └── python-tests.yml  # GitHub Actions workflow (the automation!)
└── README.md
```

---

## 🚀 Step 1: Understanding the Workflow File

Let's examine the GitHub Actions workflow file. Open `.github/workflows/python-tests.yml` and follow along:

### Workflow Structure

Every GitHub Actions workflow has these main parts:

#### 1. **Workflow Name**
```yaml
name: Python Unit Tests Demo
```
- This is just a label for your workflow (shows up in the GitHub Actions tab)

#### 2. **Triggers** (`on:`)
```yaml
on:
  push:
  pull_request:
  workflow_dispatch:
```
This tells GitHub **when** to run the workflow:
- `push:` - Runs when you push code to any branch
- `pull_request:` - Runs when someone opens or updates a pull request
- `workflow_dispatch:` - Allows you to manually trigger it from GitHub's UI

**Try it:** Make a small change to any file and push it. Watch the Actions tab!

#### 3. **Concurrency**
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
- If you push multiple times quickly, this cancels old runs and only keeps the latest one
- Prevents wasting resources on outdated tests

#### 4. **Jobs** (`jobs:`)
A job is a set of steps that run on the same machine. This workflow has one job called `test`.

#### 5. **Runner** (`runs-on:`)
```yaml
runs-on: ubuntu-24.04
```
- This specifies the operating system (Ubuntu Linux in this case)
- GitHub provides free virtual machines to run your workflows

#### 6. **Strategy Matrix**
```yaml
strategy:
  fail-fast: false
  matrix:
    python-version: ['3.12']
```
- `matrix:` lets you test on multiple Python versions (currently just 3.12)
- `fail-fast: false` means if one version fails, others still run

**Exercise:** Try adding more Python versions like `['3.9', '3.10', '3.11', '3.12']` to test on multiple versions!

#### 7. **Steps** - The Actual Work

Each step does one thing:

**Step 1: Checkout Code**
```yaml
- uses: actions/checkout@v4
```
- Downloads your repository code to the virtual machine
- `uses:` means "use this pre-made action from the GitHub Actions marketplace"

**Step 2: Set Up Python**
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: ${{ matrix.python-version }}
    cache: pip
```
- Installs Python (version from the matrix)
- `cache: pip` speeds up future runs by caching installed packages
- `${{ }}` is GitHub Actions syntax for variables

**Step 3: Install Dependencies**
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```
- `run:` executes shell commands
- Upgrades pip, then installs packages from `requirements.txt` (pytest, pytest-cov)

**Step 4: Run Tests**
```yaml
- name: Run tests with coverage
  run: |
    pytest -v test_calculator.py --cov=calculator --cov-report=xml --cov-report=term
```
- Runs pytest with verbose output (`-v`)
- `--cov=calculator` measures how much of your code is tested
- `--cov-report=xml` creates a coverage report file
- `--cov-report=term` shows coverage in the terminal

**Step 5: Upload Coverage**
```yaml
- name: Upload coverage to Codecov
  if: github.event_name == 'push'
  uses: codecov/codecov-action@v5
  with:
    file: ./coverage.xml
    fail_ci_if_error: false
```
- Only runs on pushes (not pull requests)
- Uploads coverage data to Codecov (a coverage tracking service)
- `fail_ci_if_error: false` means if Codecov fails, the workflow still passes

---

## 🧪 Step 2: Testing Locally First

Before pushing to GitHub, always test locally! Here's how:

### Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd pytest_demo
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Run Tests

**Run all tests:**
```bash
pytest test_calculator.py -v
```

**Run with coverage:**
```bash
pytest test_calculator.py --cov=calculator --cov-report=term
```

**Run a specific test:**
```bash
pytest test_calculator.py::TestAdd::test_add_positive_numbers -v
```

**Expected output:** You should see all tests passing! ✅

---

## 🎓 Step 3: Understanding the Test Results

When you run tests, you'll see output like:
```
test_calculator.py::TestAdd::test_add_positive_numbers PASSED
test_calculator.py::TestAdd::test_add_negative_numbers PASSED
...
```

- ✅ **PASSED** = Test works correctly
- ❌ **FAILED** = Something is wrong with your code
- ⚠️ **ERROR** = Test itself has a problem

**Exercise:** Try breaking a test! Change `assert add(2, 3) == 5` to `assert add(2, 3) == 6` and see what happens.

---

## 🚀 Step 4: Seeing GitHub Actions in Action

### Viewing Workflow Runs

1. Go to your repository on GitHub
2. Click the **"Actions"** tab at the top
3. You'll see a list of all workflow runs
4. Click on any run to see detailed logs

### Understanding the Results

- 🟢 **Green checkmark** = All tests passed
- 🔴 **Red X** = Tests failed (check the logs to see why)
- 🟡 **Yellow circle** = Workflow is still running

### Reading the Logs

Click on a workflow run, then click on the job name (`test`). You'll see:
- Each step expanding to show its output
- Test results with pass/fail status
- Coverage percentages
- Any error messages

**Exercise:** 
1. Make a small change (add a comment to `calculator.py`)
2. Commit and push: `git add .`, `git commit -m "test workflow"`, `git push`
3. Go to the Actions tab and watch it run!

---

## 📝 Step 5: Hands-On Exercises

Try these exercises to deepen your understanding:

### Exercise 1: Add More Python Versions
**Goal:** Test on multiple Python versions

1. Edit `.github/workflows/python-tests.yml`
2. Change the matrix to:
   ```yaml
   python-version: ['3.9', '3.10', '3.11', '3.12']
   ```
3. Commit and push
4. Watch the workflow run 4 jobs (one per Python version)!

### Exercise 2: Add a New Test
**Goal:** Practice writing tests

1. Open `test_calculator.py`
2. Add a new test in the `TestAdd` class:
   ```python
   def test_add_large_numbers(self):
       """Test adding large numbers."""
       assert add(1000000, 2000000) == 3000000
   ```
3. Run locally: `pytest test_calculator.py -v`
4. Commit and push to see it run in GitHub Actions

### Exercise 3: Break Something (On Purpose!)
**Goal:** See what happens when tests fail

1. Temporarily break the `add` function in `calculator.py`:
   ```python
   def add(a: float, b: float) -> float:
       return a + b + 1  # Wrong!
   ```
2. Commit and push
3. Check the Actions tab - you should see a red X ❌
4. Fix it and push again - should be green ✅

### Exercise 4: Add a New Step
**Goal:** Customize the workflow

1. Add a step after "Run tests with coverage" to print a message:
   ```yaml
   - name: Success message
     run: echo "All tests passed! 🎉"
   ```
2. Commit and push
3. Check the logs to see your message

---

## 🔍 Step 6: Key Concepts to Remember

### GitHub Actions Syntax

- `name:` - Label for your workflow
- `on:` - When to trigger the workflow
- `jobs:` - Groups of steps that run together
- `runs-on:` - Operating system to use
- `steps:` - Individual commands to execute
- `uses:` - Reuse an action from the marketplace
- `run:` - Execute shell commands
- `${{ }}` - Variable syntax (e.g., `${{ matrix.python-version }}`)

### Best Practices

1. **Test locally first** - Don't waste GitHub Actions minutes on simple mistakes
2. **Use caching** - Speeds up your workflows
3. **Test on multiple versions** - Ensures compatibility
4. **Read the logs** - They tell you exactly what went wrong
5. **Start simple** - Add complexity gradually

---

## 🐛 Troubleshooting

### Workflow won't run?
- Check that the file is in `.github/workflows/` (not `.github/workflow/`)
- Ensure the YAML syntax is correct (indentation matters!)
- Check the Actions tab for error messages

### Tests fail in GitHub but pass locally?
- Python version mismatch? Check the matrix
- Missing dependencies? Check `requirements.txt`
- Different operating system? Some code behaves differently on Linux vs Windows

### Can't see the Actions tab?
- Make sure you're viewing the repository on GitHub (not just locally)
- The repository needs to be pushed to GitHub (not just local)

---

## 📚 Next Steps

Now that you understand the basics:

1. **Explore other actions**: Visit [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
2. **Add more workflows**: Create workflows for linting, building, or deploying
3. **Learn about secrets**: Store sensitive data securely
4. **Try different triggers**: Schedule workflows with `cron`, or trigger on releases

---

## 📖 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [YAML Syntax Guide](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

---

## 💡 Quick Reference

### Common pytest commands:
```bash
pytest                    # Run all tests
pytest -v                 # Verbose output
pytest --cov=calculator   # With coverage
pytest path/to/test.py    # Run specific file
```

### Common GitHub Actions triggers:
```yaml
on:
  push:                   # On any push
  pull_request:           # On PRs
  workflow_dispatch:      # Manual trigger
  schedule:               # Scheduled (cron)
    - cron: '0 0 * * *'   # Daily at midnight
```

---

## 🎉 Congratulations!

You've learned the fundamentals of GitHub Actions! You can now:
- ✅ Understand workflow files
- ✅ Set up automated testing
- ✅ Interpret workflow results
- ✅ Customize workflows for your projects

Happy coding! 🚀
