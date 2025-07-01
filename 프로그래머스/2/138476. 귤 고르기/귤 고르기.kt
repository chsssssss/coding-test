class Solution {
    fun solution(k: Int, tangerine: IntArray): Int {
        var answer: Int = 0
        var dic = mutableMapOf<Int, Int>()
        var count = 0
        for (t in tangerine) {
            if (dic.containsKey(t)) {
                dic[t] = dic[t]!! + 1
            }
            else {
                dic[t] = 1
            }
        }
        var temp = dic.toList().sortedByDescending { it.second }
        for ((key, values) in temp) {
            answer = answer + 1
            for (i in 1..values) {
                count = count + 1
                if (count >= k) {
                    return answer
                }
            }
        }
        return answer
    }
}