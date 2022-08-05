import tensorflow as tf

assert "_v2.keras" in tf.keras.__name__, "Test _v2.keras in tf.keras.__name__"

t1 = tf.constant([1, 2, 3, 4])
t2 = tf.constant([5, 6, 7, 8])
assert tf.add(t1, t2).shape == (4,), "Test array shape after adding two arrays"

assert "_v2.estimator" in tf.estimator.__name__, "Test _v2.estimator in tf.estimator.__name__"
