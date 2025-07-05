class Solution {
    fun solution(num_list: IntArray, n: Int): MutableList<Int> {
        var answer: MutableList<Int> = mutableListOf()
        for (i in 0..n-1) {
            answer.add(num_list[i])
        }
        return answer
    }
}