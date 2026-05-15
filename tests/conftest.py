import copy

import pytest

from src import app


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(app.activities)
    yield
    app.activities.clear()
    app.activities.update(original_activities)
