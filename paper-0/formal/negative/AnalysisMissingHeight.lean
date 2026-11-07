import Chapter03Analysis
open AEGPaper0.Chapter03Analysis
example (p : Plane) : HasFDerivAt AEGPaper0.Chapter03Coordinates.assignment (assignmentDerivative p) p := by
  exact assignment_hasFDerivAt p
