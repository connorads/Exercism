(ns armstrong-numbers)

(defn digits [n]
  (->> n str (map (comp read-string str))))

(defn pow [exp x]
  (reduce * 1 (repeat exp x)))

(defn sumToThePowerOfN [n coll]
  (let [powToN (partial pow n)]
    (reduce + (map powToN coll))))

(defn armstrong? [num]
  (let [digits (digits num)]
    (let [noDigits (count digits)]
      (= num (sumToThePowerOfN noDigits digits)))))