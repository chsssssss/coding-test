import kotlin.math.abs
class Solution {
    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        var answer: Int = 0
        
        fun toMinutes(time: Int): Int {
            val h = time / 100
            val m = time % 100
            return h * 60 + m
        }
        
        for (i in schedules.indices) {
            var is_check = true
            for (j in 0 until 7) {
                val day = (startday + j - 1) % 7 + 1
                
                if (day == 6 || day == 7) continue
                
                if ( toMinutes(schedules[i]) + 10 < toMinutes(timelogs[i][j])) {
                    is_check = false
                }
            }
            if (is_check) {
                answer += 1
            }
            
        }
        return answer
    }
}