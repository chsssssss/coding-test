class Solution {
    fun solution(a: Int, b: Int): Int {
        val ab = (a.toString() + b.toString()).toInt()
        val ba = (b.toString() + a.toString()).toInt()
        if (ab < ba) {
            return ba
        }
        else {
            return ab
        }
    }
}