# Git Bisect Demo

This is a simple Python calculator project designed to demonstrate basic
arithmetic operations. The project includes multiple commits, with one commit
intentionally introducing a bug. This setup can be used to demonstrate how to
use `git bisect` to locate and fix bugs in a project.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Exponentiation (Power)
- Modulus

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aedrax/git-bisect-demo.git
   cd git-bisect-demo
   ```

2. Ensure you have Python installed (at least Python 3.6).

## Usage

To use the calculator, run the `calculator.py` script:

```bash
python calculator.py
```

This will perform some basic calculations and print the results to the console.

## Testing

To test the calculator functions, you can run the newly added tests using:

```bash
python -m unittest discover tests
```

Oh no! A bug was discovered!

## Demonstration of Bug and `git bisect`

This project contains a bug intentionally introduced in one of the commits. The 
bug causes the `mult` function to subtract 1 after multiplying. (Sure we can
git blame because we can see exactly where the bug is, but assume we don't even
know what line in our potentially giant codebase is breaking things)

### Using `git bisect`

1. Start the bisect process:
   ```bash
   git bisect start
   ```

2. Mark the current commit as bad (where the bug is present):
   ```bash
   git bisect bad
   ```

3. Mark an earlier commit as good (where the bug is absent). Use the commit hash
of a known good commit:
   ```bash
   git bisect good <commit-hash>
   ```

4. `git bisect` will now checkout different commits. Run the `calculator.py` 
script to see if the bug is present

5. Mark each commit as good or bad:
   - If the bug is present: `git bisect bad`
   - If the bug is absent: `git bisect good`

6. Repeat until `git bisect` identifies the commit that introduced the bug.

7. After identifying the problematic commit you conclude the bisect process:
   ```bash
   git bisect reset
   ```

### Automating with `git bisect run`

Instead of running the tests manually, you can use `git bisect run`.
This will automatically run the tests and determine if a commit contains the bug
or is another good commit.

For this repo, our unit tests weren't added until much later. So we'll make a
quick script to determine if the bug is present in the commit.

Create a file `/tmp/test_multiply.sh` with the following content:

```bash
#!/bin/bash
set -e

# Temporary Python script to test the multiply function
cat <<EOF > /tmp/test_multiply.py
import sys
import os

# Add the current working directory to the Python path
sys.path.insert(0, os.getcwd())

from calculator import mult

def test_multiply():
    assert mult(3, 4) == 12
    assert mult(-1, 1) == -1
    assert mult(-1, -1) == 1
    assert mult(0, 5) == 0

if __name__ == "__main__":
    try:
        test_multiply()
    except AssertionError:
        sys.exit(1)
EOF

# Run the temporary Python script
python /tmp/test_multiply.py

```

Make the script executable:

```bash
chmod +x /tmp/test_multiply.sh
```

Repeat steps 1-5 of **Using git bisect** but now instead of manually testing, run
the following:

```bash
git bisect run /tmp/test_multiply.sh
```

This will automatically do all the checks!
