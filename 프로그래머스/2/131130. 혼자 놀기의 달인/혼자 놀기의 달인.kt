class Solution {
    fun solution(cards: IntArray): Int {
        var answer: Int = 0
        val visited = BooleanArray(cards.size)
        val groups = mutableListOf<Int>()
        for (i in cards.indices) {
            var count: Int = 0
            var current: Int = i
            
            if (visited[i]) continue

            while (!visited[current]) {
                visited[current] = true
                current = cards[current] - 1
                count ++
            }
            groups.add(count)   
        }
        
        if (groups.size < 2) return 0
        
        groups.sortDescending()
            
        return groups[0] * groups[1]
    }
}