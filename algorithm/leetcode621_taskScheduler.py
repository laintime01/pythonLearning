import heapq


class Solution(object):
    def taskScheduler(self, tasks, n):
        """
        :param tasks: List[str]
        :param n:int
        :return:int
        """
        task_dict = {}
        for task in tasks:
            task_dict[task] = task_dict.get(task, 0) + 1

        heap = [[-cnt, task] for task, cnt in task_dict.items()]
        heapq.heapify(heap)

        res = 0
        while True:
            round_task = []
            for index in range(n + 1):
                if heap:
                    round_task.append(heapq.heappop(heap))
                    round_task[-1][0] += 1
            print(f'round->{round_task}')

            for cnt, task in round_task:
                if cnt < 0:
                    heapq.heappush(heap, [cnt, task])

            if heap:
                res += n + 1
            else:
                return res + len(round_task)


tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(Solution().taskScheduler(tasks, n))
