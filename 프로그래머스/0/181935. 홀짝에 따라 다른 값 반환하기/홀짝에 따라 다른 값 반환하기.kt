class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        if (n%2 == 1) {
            for (i in 0..n) {
                if (i%2 == 1) {
                    answer = answer + i
                }
            }
        }
        else {
            for (i in 0..n) {
                if (i%2 == 0) {
                    answer = answer + i*i
                }
            }
        }
        return answer
    }
}