class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        val fibo = arrayListOf(0, 1)
        for (i in 2..n) {
            fibo.add((fibo[i - 1] + fibo[i - 2]) % 1234567)
        }
        return fibo[n]
    }
}