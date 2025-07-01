class Solution {
    fun solution(elements: IntArray): Int {
        var answer: Int = 0
        val n = elements.size
        val extended = IntArray(n * 2)
        for (i in elements.indices) {
            extended[i] = elements[i]
            extended[i + n] = elements[i]
        }
        val sum = mutableSetOf<Int>()
        
        for (start in 0 until n) {
            var acc = 0
            for (len in 1..n) {
                acc += extended[start + len - 1]
                sum.add(acc)
            }
        }
        return sum.size
    }
}