def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": -0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Aspartate_Aminotransferase", "instances": 122, "metric_value": -0.0, "depth": 4}
            if obj[5]<=66.18852459016394:
               # {"feature": "Direct_Bilirubin", "instances": 90, "metric_value": -0.0, "depth": 5}
               if obj[2]<=6:
                  # {"feature": "Total_Bilirubin", "instances": 75, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Total_Protiens", "instances": 50, "metric_value": -0.0, "depth": 7}
                     if obj[6]>14.482825371546518:
                        # {"feature": "Alamine_Aminotransferase", "instances": 43, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=31.023255813953487:
                           return 'liver'
                        elif obj[4]>31.023255813953487:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=14.482825371546518:
                        # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=7:
                     # {"feature": "Alkaline_Phosphotase", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Protiens", "instances": 22, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=67:
                           return 'liver'
                        elif obj[6]>67:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[3]>291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=24:
                           return 'liver'
                        elif obj[4]>24:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>6:
                  # {"feature": "Total_Protiens", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=78:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[1]>17:
                        return 'liver'
                     elif obj[1]<=17:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[4]>18:
                           return 'liver'
                        elif obj[4]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>78:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[5]>66.18852459016394:
               # {"feature": "Alkaline_Phosphotase", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[1]>15:
                     # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=28:
                        # {"feature": "Total_Protiens", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[6]>62:
                           return 'liver'
                        elif obj[6]<=62:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>28:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=15:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alamine_Aminotransferase", "instances": 30, "metric_value": 0.0, "depth": 4}
            if obj[4]>14:
               # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[5]>17:
                  # {"feature": "Total_Protiens", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[6]>61:
                     # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=9:
                           return 'liver'
                        elif obj[1]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=61:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=17:
                  return 'normal'
               else:
                  return 'normal'
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
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[8]<=13.838983050847459:
            # {"feature": "Alkaline_Phosphotase", "instances": 100, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 71, "metric_value": 0.0, "depth": 5}
               if obj[1]>1:
                  # {"feature": "Direct_Bilirubin", "instances": 67, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Protiens", "instances": 56, "metric_value": 0.0, "depth": 7}
                     if obj[6]>50.714285714285715:
                        # {"feature": "Alamine_Aminotransferase", "instances": 37, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=107.24740440212926:
                           return 'liver'
                        elif obj[4]>107.24740440212926:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=50.714285714285715:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[5]>29:
                           return 'liver'
                        elif obj[5]<=29:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=50:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>50:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=1:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=58:
                           return 'normal'
                        elif obj[6]>58:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 29, "metric_value": 0.0, "depth": 5}
               if obj[2]<=31.896551724137932:
                  return 'liver'
               elif obj[2]>31.896551724137932:
                  # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[6]>55:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[1]>68:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]>39:
                           return 'liver'
                        elif obj[4]<=39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=68:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=55:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]>13.838983050847459:
            # {"feature": "Alkaline_Phosphotase", "instances": 18, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[5]>28:
                  # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[2]>2:
                     return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>21:
                        return 'liver'
                     elif obj[4]<=21:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]<=28:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[2]>3:
                  return 'liver'
               elif obj[2]<=3:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>17:
                        return 'normal'
                     elif obj[4]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=5:
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[6]<=84.16676164311447:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 109, "metric_value": -0.0, "depth": 5}
               if obj[8]<=27.40366972477064:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 91, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=143.46153846153845:
                     # {"feature": "Total_Bilirubin", "instances": 76, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=33:
                        # {"feature": "Alamine_Aminotransferase", "instances": 71, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=37.49295774647887:
                           return 'normal'
                        elif obj[4]>37.49295774647887:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>33:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>143.46153846153845:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[4]>48:
                        return 'liver'
                     elif obj[4]<=48:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>18:
                           return 'liver'
                        elif obj[1]<=18:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>27.40366972477064:
                  # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[4]>19:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=39:
                           return 'liver'
                        elif obj[1]>39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=19:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[6]>84.16676164311447:
               # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[5]>19:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        return 'normal'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[5]<=19:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 38, "metric_value": -0.0, "depth": 4}
            if obj[1]>8:
               # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 5}
               if obj[5]<=231.04347826086956:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[8]>8:
                     # {"feature": "Total_Protiens", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[6]>59:
                        return 'liver'
                     elif obj[6]<=59:
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
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]>15:
                           return 'liver'
                        elif obj[4]<=15:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[5]>231.04347826086956:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[1]<=8:
               # {"feature": "Total_Protiens", "instances": 15, "metric_value": -0.0, "depth": 5}
               if obj[6]>69:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[4]>25:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[5]>35:
                           return 'liver'
                        elif obj[5]<=35:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=25:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=69:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]>9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=70:
                           return 'liver'
                        elif obj[4]>70:
                           return 'normal'
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
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 75, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 55, "metric_value": 0.0, "depth": 5}
               if obj[4]>11:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 54, "metric_value": 0.0, "depth": 6}
                  if obj[5]>13:
                     # {"feature": "Direct_Bilirubin", "instances": 53, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Total_Bilirubin", "instances": 41, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=11:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 5}
               if obj[4]>25:
                  # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[1]>23:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[2]>15:
                        return 'liver'
                     elif obj[2]<=15:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=57:
                           return 'normal'
                        elif obj[5]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]<=23:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=25:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'normal'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alkaline_Phosphotase", "instances": 20, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=28:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>6:
                           return 'liver'
                        elif obj[6]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>28:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=8:
                           return 'liver'
                        elif obj[6]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]<=1:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]>48:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]>4:
                        return 'liver'
                     elif obj[2]<=4:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=48:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=30:
                     # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=8:
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
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
