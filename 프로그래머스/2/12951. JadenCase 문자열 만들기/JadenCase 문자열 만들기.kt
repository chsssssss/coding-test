class Solution {
    fun solution(s: String): String {
        var answer = ""
        var newWord = true
        for (i in s) {
            when {
                i == ' ' -> {
                    answer = answer + ' '
                    newWord = true
                }
                
                newWord -> {
                    answer = answer + i.uppercaseChar()
                    newWord = false
                }
                
                else -> {
                    answer = answer + i.lowercaseChar()
                }
            }
        }
        return answer
    }
}