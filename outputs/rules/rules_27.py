def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 122, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 91, "metric_value": 0.0, "depth": 5}
               if obj[6]>5:
                  # {"feature": "Alamine_Aminotransferase", "instances": 90, "metric_value": -0.0, "depth": 6}
                  if obj[4]>10:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 89, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=55.561797752808985:
                        # {"feature": "Total_Bilirubin", "instances": 66, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=22:
                           return 'liver'
                        elif obj[1]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>55.561797752808985:
                        # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=94:
                           return 'liver'
                        elif obj[1]>94:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=5:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": 0.0, "depth": 5}
               if obj[1]>6:
                  # {"feature": "Direct_Bilirubin", "instances": 30, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=12:
                     # {"feature": "Total_Protiens", "instances": 17, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=68:
                        return 'liver'
                     elif obj[6]>68:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>29:
                           return 'liver'
                        elif obj[4]<=29:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>12:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=6:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alamine_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 4}
            if obj[4]>14:
               # {"feature": "Total_Protiens", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[6]<=68:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[5]>20:
                     return 'liver'
                  elif obj[5]<=20:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]>68:
                  # {"feature": "Alkaline_Phosphotase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[4]<=14:
               # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     return 'normal'
                  elif obj[1]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[6]>23.646973828484313:
               # {"feature": "Direct_Bilirubin", "instances": 64, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 57, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=39.87719298245614:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=11:
                        # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>11:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=32:
                           return 'liver'
                        elif obj[5]>32:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>39.87719298245614:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=8:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]>22:
                           return 'liver'
                        elif obj[1]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>8:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=4:
                           return 'liver'
                        elif obj[1]>4:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=5:
                        return 'liver'
                     elif obj[1]>5:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>20:
                           return 'normal'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[8]<=5:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=23.646973828484313:
               # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=50:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=37:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>37:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>50:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     return 'liver'
                  elif obj[5]<=23:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[8]<=6:
               # {"feature": "Total_Protiens", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[6]<=55:
                  return 'liver'
               elif obj[6]>55:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[5]>64:
                     return 'liver'
                  elif obj[5]<=64:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=73:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>8:
                           return 'normal'
                        elif obj[2]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>73:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>6:
               # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[1]>15:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]>69:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>105:
                           return 'normal'
                        elif obj[5]<=105:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=69:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=15:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[2]>5:
                     return 'liver'
                  elif obj[2]<=5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>16:
                        return 'normal'
                     elif obj[4]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": -0.0, "depth": 4}
            if obj[8]<=26.155172413793103:
               # {"feature": "Direct_Bilirubin", "instances": 98, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Protiens", "instances": 84, "metric_value": 0.0, "depth": 6}
                  if obj[6]>12.950746527305796:
                     # {"feature": "Total_Bilirubin", "instances": 72, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=86.32686847564696:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 67, "metric_value": 0.0, "depth": 8}
                        if obj[5]>11:
                           return 'liver'
                        elif obj[5]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>86.32686847564696:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=12.950746527305796:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]>33:
                        return 'liver'
                     elif obj[4]<=33:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'normal'
                        elif obj[5]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[5]>31:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]>22:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=7:
                           return 'liver'
                        elif obj[6]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=22:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=31:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>24:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=69:
                           return 'liver'
                        elif obj[6]>69:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=24:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>26.155172413793103:
               # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[1]<=19:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 6}
                  if obj[5]>31:
                     # {"feature": "Total_Protiens", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[6]>68:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'liver'
                        elif obj[4]<=18:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=68:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=31:
                     # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[6]>61:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=61:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>19:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": -0.0, "depth": 4}
            if obj[6]<=72:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[8]>7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=84:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>34:
                           return 'liver'
                        elif obj[5]<=34:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>84:
                     # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'liver'
                     elif obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]<=7:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[5]>44:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=44:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        return 'liver'
                     elif obj[1]>9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>72:
               # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 5}
               if obj[1]<=9:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=7:
                           return 'liver'
                        elif obj[8]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=28:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'liver'
                        elif obj[2]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=23:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        return 'normal'
                     elif obj[2]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[1]>9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]>29:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>42:
                           return 'liver'
                        elif obj[5]<=42:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=29:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 75, "metric_value": -0.0, "depth": 4}
            if obj[6]>51.76:
               # {"feature": "Alkaline_Phosphotase", "instances": 56, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 40, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=71.625:
                     # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[4]>21:
                           return 'normal'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>71.625:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=82:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[5]>24:
                        # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[4]>48:
                           return 'liver'
                        elif obj[4]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=24:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>82:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=51.76:
               # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[1]<=8:
                  # {"feature": "Alkaline_Phosphotase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=29:
                           return 'normal'
                        elif obj[4]>29:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'normal'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[1]>8:
                  # {"feature": "Alkaline_Phosphotase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>37:
                           return 'liver'
                        elif obj[4]<=37:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]>3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>10:
                           return 'liver'
                        elif obj[4]<=10:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 4}
            if obj[1]>8:
               # {"feature": "Alkaline_Phosphotase", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>20:
                     # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=8:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>8:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=20:
                     # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=6:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=4:
                        return 'normal'
                     elif obj[2]>4:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[1]<=8:
               # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Protiens", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>26:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=6:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
