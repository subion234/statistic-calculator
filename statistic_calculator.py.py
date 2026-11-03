def get_user_data():
    """Collects numbers from user until they type 'done' or 'q'."""
    data = []
    print("--- Enter numbers one by one ---")
    print("Type 'done' or 'q' when finished.\n")
    
    while True:
        user_input = input("Enter a number: ").strip()
        if user_input.lower() in ["done", "q"]:
            break
        try:
            val = float(user_input)
            data.append(val)
        except ValueError:
            print("Invalid entry! Please enter a valid number or 'done'/'q' to finish.")
            
    return data


def calculate_mean(data):
    """Calculates the arithmetic average."""
    return sum(data) / len(data)


def calculate_median(data):
    """Calculates the middle value of a sorted dataset."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 != 0:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0


def calculate_mode(data):
    """Calculates the most frequent value(s)."""
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
        
    max_count = max(counts.values())
    
    # If all items appear the same number of times, there is no distinct mode
    if max_count == 1:
        return "No mode (all values appear once)"
        
    modes = [val for val, count in counts.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes


def calculate_range(data):
    """Calculates the difference between maximum and minimum values."""
    return max(data) - min(data)


def calculate_variance(data, is_sample=True):
    """Calculates variance (sample by default)."""
    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    
    # Use n - 1 for sample variance if n > 1, else population variance n
    divisor = len(data) - 1 if is_sample and len(data) > 1 else len(data)
    return sum(squared_diffs) / divisor


def calculate_std_dev(variance):
    """Calculates standard deviation from variance."""
    return variance ** 0.5


def main():
    print("=======================================")
    print("       PYTHON STATISTICS CALCULATOR    ")
    print("=======================================\n")
    
    data = get_user_data()
    
    # Step 3: Handle edge cases
    if not data:
        print("\n[Error] No valid data was entered. Exiting program.")
        return
        
    # Step 2: Perform calculations
    mean_val = calculate_mean(data)
    median_val = calculate_median(data)
    mode_val = calculate_mode(data)
    range_val = calculate_range(data)
    variance_val = calculate_variance(data)
    std_dev_val = calculate_std_dev(variance_val)
    
    # Step 4: Display results
    print("\n---------------------------------------")
    print(f"Dataset: {data}")
    print(f"Total Count (n): {len(data)}")
    print("---------------------------------------")
    print(f"Mean:               {mean_val:.3f}")
    print(f"Median:             {median_val:.2f}")
    
    if isinstance(mode_val, list):
        formatted_modes = ", ".join([f"{m:.2f}" for m in mode_val])
        print(f"Mode(s):            {formatted_modes}")
    elif isinstance(mode_val, (int, float)):
        print(f"Mode:               {mode_val:.2f}")
    else:
        print(f"Mode:               {mode_val}")
        
    print(f"Range:              {range_val:.2f}")
    print(f"Sample Variance:    {variance_val:.2f}")
    print(f"Sample Std Dev:     {std_dev_val:.2f}")
    print("---------------------------------------")


if __name__ == "__main__":
    main()
