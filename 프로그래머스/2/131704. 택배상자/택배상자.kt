class Solution {
    fun solution(order: IntArray): Int {
        var answer: Int = 0
        val stack = mutableListOf<Int>()
        
        var order_idx = 0
        
        for (i in 1..order.size) {
            stack.add(i)
            
            while(stack.isNotEmpty() && order[order_idx] == stack.last()) {
                stack.removeAt(stack.size -1)
                answer ++
                order_idx ++
            }
        }
        
        return answer
    }
}