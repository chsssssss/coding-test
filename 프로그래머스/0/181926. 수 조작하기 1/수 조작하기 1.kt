class Solution {
    fun solution(n: Int, control: String): Int {
        var answer: Int = 0
        answer = n
        for (i in control) {
            if (i == 'w') {
                answer = answer + 1
            }
            else if(i == 's') {
                answer = answer - 1
            }
            else if(i == 'd') {
                answer = answer + 10
            }
            else if(i == 'a') {
                answer = answer - 10
            }
        }
        return answer
    }
}