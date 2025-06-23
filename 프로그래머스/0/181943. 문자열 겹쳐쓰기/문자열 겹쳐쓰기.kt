class Solution {
    fun solution(my_string: String, overwrite_string: String, s: Int): String {
        var answer: String = ""
        answer += my_string.substring(0, s)
        answer += overwrite_string
        if (s + overwrite_string.length < my_string.length) {
            answer += my_string.substring(s + overwrite_string.length, my_string.length)
        }
        
        
        print(answer)
        return answer    
    }
}
                