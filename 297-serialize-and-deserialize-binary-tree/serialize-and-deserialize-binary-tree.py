from collections import deque

class Codec:

    def serialize(self, root):
        if root is None:
            return ""

        arr = []
        q = deque([root])

        while q:
            cur = q.popleft()

            if cur:
                arr.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                arr.append("N")

        return ",".join(arr)

    def deserialize(self, data):
        if not data:
            return None

        data = data.split(",")

        root = TreeNode(int(data[0]))
        q = deque([root])

        i = 1

        while q:
            cur = q.popleft()

            if data[i] != "N":
                cur.left = TreeNode(int(data[i]))
                q.append(cur.left)

            i += 1

            if data[i] != "N":
                cur.right = TreeNode(int(data[i]))
                q.append(cur.right)

            i += 1

        return root