class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        if ((a.toString()+b.toString()).toInt() < 2*a*b) {
            return 2*a*b
        }
        else {
            return (a.toString() + b.toString()).toInt()
        }

    }
}