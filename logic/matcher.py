import numpy as np

def match_pitch(detected_pitch, target_pitches, tolerance=0.05):
  matched = 0
  for target in target_pitches:
    if abs(detected_pitch - target) / target < tolerance:
      matched += 1

  match_rate = (matched / len(target_pitches)) * 100
  return round(match_rate)
