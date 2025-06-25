class Solution {
    fun solution(str1: String, str2: String): String {
        var answer: String = ""
        for(i in 0 until str1.length + str2.length) {
            if (i % 2 == 0) {
                answer = answer + str1[i/2]
            }
            else {
                answer = answer + str2[i/2]
            }
        }
        return answer
    }
}