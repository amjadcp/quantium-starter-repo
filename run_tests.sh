#!/bin/bash

# 1. Path to your virtual environment (update 'venv' to your folder name)
VENV_PATH="./venv/bin/activate"

# 2. Activate the virtual environment
if [ -f "$VENV_PATH" ]; then
    source "$VENV_PATH"
else
    echo "Error: Virtual environment not found at $VENV_PATH"
    exit 1
fi

# 3. Execute the test suite using pytest
# We use 'pytest' directly. It returns non-zero exit codes on failure.
pytest --webdriver Chrome --headless ./test_visualise_pink_morsels_daily_sales.py

# 4. Capture the exit code of the last command (pytest)
TEST_RESULT=$?

# 5. Logic to return 0 on success or 1 on failure
if [ $TEST_RESULT -eq 0 ]; then
    echo "------------------------------------"
    echo "TESTS PASSED SUCCESSFULLY"
    echo "------------------------------------"
    exit 0
else
    echo "------------------------------------"
    echo "TESTS FAILED WITH EXIT CODE $TEST_RESULT"
    echo "------------------------------------"
    exit 1
fi
