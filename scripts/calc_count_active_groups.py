import json

from src.config.config import Config
from src.models.origin_schedule_model import OriginScheduleModel
from src.repositories.schedule_repository import ScheduleRepository

# 380 / 191

config = Config(path_env="../.env")

with open("all_groups_02112025.json", encoding="utf-8") as f:
    all_groups = json.loads(f.read())

schedule_repository = ScheduleRepository(base_url=config.base_schedule_api_url)
count_active = 0

for index, group in enumerate(all_groups):
    group_name = group["groupName"]
    print(f"{index+1}/{len(all_groups)}: {group_name}", end=" ")
    group_id = group["id"]
    response = schedule_repository.fetch_group(group_id=group_id, date_start="2025-10-27", date_end="2025-11-02")
    is_active = response.schedule != OriginScheduleModel()
    if not is_active:
        response = schedule_repository.fetch_group(group_id=group_id, date_start="2025-10-20", date_end="2025-11-26")
        is_active = response.schedule != OriginScheduleModel()
    if is_active:
        count_active += 1

    print(f"is {"" if is_active else "not "}active\nTotal active groups: {count_active}")

print(f"Complete!\nTotal groups: {len(all_groups)}\nTotal active groups: {count_active}")
