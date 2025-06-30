class Solution {
    fun solution(code: String): String {
        var answer: String = ""
        var mode: Int = 0
        for (i in code.indices) {
            if (mode == 0) {
                if (code[i] == '1') {
                    mode = 1
                }
                else {
                    if(i % 2 == 0) {
                        answer = answer + code[i]
                    }
                }
            }
            else {
                if (code[i] == '1') {
                    mode = 0
                }
                else {
                    if(i % 2 == 1) {
                        answer = answer + code[i]
                    }
                }
            }
        }
        if (answer.isEmpty()) {
            return "EMPTY"
        }
        return answer
    }
}