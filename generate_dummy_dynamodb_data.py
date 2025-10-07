import random
import json
import csv
from datetime import datetime, timedelta


def generate_dummy_item():
    """Generate one random DynamoDB-like item"""
    actions = ['like', 'comment', 'follow', 'view', 'share', 'save']
    user_id = f"user_{random.randint(1, 1000)}"
    activity_id = f"activity_{random.randint(100000, 999999)}"
    expire_at = int((datetime.utcnow() + timedelta(days=random.randint(1, 30))).timestamp())

    item = {
        "user_id": user_id,
        "activity_id": activity_id,
        "action": random.choice(actions),
        "timestamp": datetime.utcnow().isoformat(),
        "expire_at": expire_at
    }
    return item


def generate_data(count=1000):
    """Generate multiple random items"""
    data = [generate_dummy_item() for _ in range(count)]
    return data


def save_as_json(data, filename="dynamodb_sample_data.json"):
    """Save data to a local JSON file"""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ {len(data)} records saved to {filename}")


def save_as_csv(data, filename="dynamodb_sample_data.csv"):
    """Save data to a local CSV file"""
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ {len(data)} records saved to {filename}")


if __name__ == "__main__":
    # You can modify count here
    num_records = 1000
    dummy_data = generate_data(num_records)

    # Save in both formats (optional)
    save_as_json(dummy_data)
    save_as_csv(dummy_data)
