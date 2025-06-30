class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        var odd: String = ""
        var even: String = ""
        for (i in num_list) {
            if (i % 2 == 0) {
                even = even + i
            }
            else {
                odd = odd + i
            }
        }
        answer = odd.toInt() + even.toInt()
        return answer
    }
}