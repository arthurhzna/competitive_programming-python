from leetcode.medium.p3228 import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    assert sol.maxOperations("1001101") == 4, "Example 1 failed"
    print("✓ Example 1 passed")
    
    # Example 2
    assert sol.maxOperations("00111") == 0, "Example 2 failed"
    print("✓ Example 2 passed")
    
    # Additional test cases
    assert sol.maxOperations("1") == 0, "Single '1' failed"
    print("✓ Single '1' passed")
    
    assert sol.maxOperations("0") == 0, "Single '0' failed"
    print("✓ Single '0' passed")
    
    assert sol.maxOperations("10") == 0, "Test '10' failed"
    print("✓ Test '10' passed")
    
    assert sol.maxOperations("101") == 1, "Test '101' failed"
    print("✓ Test '101' passed")
    
    print("\nAll tests passed!")

if __name__ == "__main__":
    test_solution()

