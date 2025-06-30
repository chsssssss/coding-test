class Solution {
    fun solution(n: Int): Int {
        var min: Int = 1000000
        for (i in 1 until n) {
            if (n % i == 1 && i < min) {
                min = i
            }
        }
        return min
    }
}