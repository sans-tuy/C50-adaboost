def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alamine_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[4]<=50.125:
            # {"feature": "Total_Protiens", "instances": 108, "metric_value": -0.0, "depth": 4}
            if obj[6]>61.52777777777778:
               # {"feature": "Alkaline_Phosphotase", "instances": 79, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 67, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=30.35820895522388:
                     # {"feature": "Direct_Bilirubin", "instances": 42, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Total_Bilirubin", "instances": 40, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>6:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>14:
                           return 'liver'
                        elif obj[1]<=14:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>30.35820895522388:
                     # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=89:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>17:
                           return 'liver'
                        elif obj[5]<=17:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>89:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=61.52777777777778:
               # {"feature": "Total_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 5}
               if obj[1]>7:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=14:
                     # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[5]>18:
                           return 'normal'
                        elif obj[5]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>14:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=7:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[5]>14:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=14:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'normal'
                        elif obj[2]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[4]>50.125:
            # {"feature": "Alkaline_Phosphotase", "instances": 44, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[2]>6:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=202:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=29:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[8]>6:
                           return 'liver'
                        elif obj[8]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>29:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>202:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=6:
                  # {"feature": "Total_Protiens", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=66:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>45:
                        return 'liver'
                     elif obj[5]<=45:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]>66:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>73:
                           return 'normal'
                        elif obj[5]<=73:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[1]>1:
               # {"feature": "Total_Protiens", "instances": 77, "metric_value": 0.0, "depth": 5}
               if obj[6]>46.42857142857143:
                  # {"feature": "Alamine_Aminotransferase", "instances": 50, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=41.54:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=16:
                        # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>16:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>28:
                           return 'liver'
                        elif obj[5]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]>41.54:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=330:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=7:
                           return 'liver'
                        elif obj[8]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>330:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=46.42857142857143:
                  # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[5]>32:
                           return 'liver'
                        elif obj[5]<=32:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=50:
                           return 'liver'
                        elif obj[4]>50:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
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
            elif obj[1]<=1:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[2]<=3:
                  # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[4]>22:
                     # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=53:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=13:
                           return 'normal'
                        elif obj[5]>13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]<=22:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]<=29.27027027027027:
               # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": -0.0, "depth": 5}
               if obj[1]>19:
                  # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=54:
                     return 'liver'
                  elif obj[6]>54:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[4]>62:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=285:
                           return 'normal'
                        elif obj[5]>285:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=62:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=19:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[5]>18:
                        # {"feature": "Total_Protiens", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[6]>6:
                           return 'liver'
                        elif obj[6]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>29.27027027027027:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[8]<=5:
                  return 'liver'
               elif obj[8]>5:
                  # {"feature": "Total_Protiens", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=55:
                     return 'liver'
                  elif obj[6]>55:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": -0.0, "depth": 7}
                     if obj[1]>68:
                        return 'normal'
                     elif obj[1]<=68:
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
         # {"feature": "Total_Protiens", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[6]>63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 110, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 78, "metric_value": 0.0, "depth": 5}
               if obj[5]<=71.96153846153847:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 63, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=12:
                     # {"feature": "Direct_Bilirubin", "instances": 39, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>12:
                     # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[5]>71.96153846153847:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=28:
                     # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[1]>18:
                        return 'liver'
                     elif obj[1]<=18:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>28:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>55:
                           return 'liver'
                        elif obj[4]<=55:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 32, "metric_value": -0.0, "depth": 5}
               if obj[8]>8:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=68:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=15:
                           return 'normal'
                        elif obj[1]>15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>68:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=21:
                           return 'liver'
                        elif obj[1]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=23:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[4]>28:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=28:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'normal'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=63.0:
            # {"feature": "Total_Bilirubin", "instances": 44, "metric_value": -0.0, "depth": 4}
            if obj[1]>6:
               # {"feature": "Direct_Bilirubin", "instances": 32, "metric_value": -0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=80:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=79:
                           return 'liver'
                        elif obj[5]>79:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>80:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[4]>19:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=105:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[8]>9:
                           return 'liver'
                        elif obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>105:
                        # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=19:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>12:
                           return 'normal'
                        elif obj[5]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[1]<=6:
               # {"feature": "Alkaline_Phosphotase", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[8]>8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        return 'liver'
                     elif obj[4]<=25:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]<=8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[5]>68:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=68:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
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
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[6]<=69.21614882171913:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 61, "metric_value": -0.0, "depth": 5}
               if obj[8]<=7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=55.6:
                     # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=23:
                           return 'normal'
                        elif obj[5]>23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>3:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]>13:
                           return 'liver'
                        elif obj[1]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>55.6:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[2]>3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]>74:
                           return 'liver'
                        elif obj[5]<=74:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>33:
                           return 'liver'
                        elif obj[5]<=33:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>7:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 26, "metric_value": 0.0, "depth": 6}
                  if obj[5]>10:
                     # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=72:
                        # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>72:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=10:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>69.21614882171913:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[4]<=45:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]>21:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=21:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>45:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[8]>9:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'normal'
                     elif obj[1]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=9:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[6]>6:
               # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 5}
               if obj[4]>30:
                  # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[2]>12:
                     return 'liver'
                  elif obj[2]<=12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=86:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[8]>7:
                           return 'normal'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>86:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=30:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>11:
                           return 'normal'
                        elif obj[2]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=6:
               # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[2]>4:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=13:
                     return 'normal'
                  elif obj[1]>13:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=4:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
