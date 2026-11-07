import Chapter04Apollonius
open AEGPaper0.Chapter04Apollonius

example (q p k : ℝ) (hk : 0 ≤ k) :
    weightedLocus q p k = Metric.sphere (center q p k : ℂ) (circleRadius q p k) := by
  exact weighted_locus_is_metric_circle q p k hk
