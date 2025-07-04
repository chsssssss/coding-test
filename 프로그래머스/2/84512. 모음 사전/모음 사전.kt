class Solution {
    
    fun solution(word: String): Int {
        val vowels = listOf("A", "E", "I", "O", "U")
        val weight = intArrayOf(781, 156, 31, 6, 1)
        var answer = 0
        for (i in word.indices) {
            val char = word[i].toString()
            val index = vowels.indexOf(char)
            answer += index * weight[i] + 1
        }
        return answer
    }
    
}