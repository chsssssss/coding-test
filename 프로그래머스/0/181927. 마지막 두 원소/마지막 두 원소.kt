class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: ArrayList<Int> = ArrayList()
        val index: Int = num_list.size - 1
        if (num_list[index] > num_list[index - 1]) {
            return num_list + (num_list[index] - num_list[index - 1])
        }
        else {
            return num_list + (num_list[index] * 2)
        }
    }
}