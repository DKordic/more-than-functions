(defn sum-to [n]
  (future (reduce + (range n))))
