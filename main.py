def classify_battery_by_soh(present_capacity, rated_capacity=120):
    soh = (present_capacity / rated_capacity) * 100
    if soh > 80:
        return "healthy"
    elif 62 <= soh <= 80:
        return "exchange"
    else:
        return "failed"
      
def count_batteries_by_health(present_capacities):
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
 for capacity in present_capacities:
        soh_category = classify_battery_by_soh(capacity)
        counts[soh_category] += 1

    return counts

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
