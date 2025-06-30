class Solution {
    fun solution(a: Int, d: Int, included: BooleanArray): Int {
        var answer: Int = 0
        var temp: Int = a
        for(i in included.indices) {
            if (included[i] == true) {
                answer = answer + temp
            }
            temp = temp + d
        }
        return answer
    }
}