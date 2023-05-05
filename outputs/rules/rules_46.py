def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 117, "metric_value": -0.0, "depth": 4}
            if obj[1]<=12.914529914529915:
               # {"feature": "Total_Protiens", "instances": 91, "metric_value": -0.0, "depth": 5}
               if obj[6]>61.18681318681319:
                  # {"feature": "Direct_Bilirubin", "instances": 66, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 59, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=15:
                        # {"feature": "Alamine_Aminotransferase", "instances": 54, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=31.51851851851852:
                           return 'liver'
                        elif obj[4]>31.51851851851852:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>15:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>10:
                           return 'liver'
                        elif obj[4]<=10:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>4:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[5]>42:
                        return 'liver'
                     elif obj[5]<=42:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        elif obj[8]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=61.18681318681319:
                  # {"feature": "Alamine_Aminotransferase", "instances": 25, "metric_value": -0.0, "depth": 6}
                  if obj[4]>13:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=45:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[8]>11:
                           return 'normal'
                        elif obj[8]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>45:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=13:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>14:
                           return 'normal'
                        elif obj[5]<=14:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[1]>12.914529914529915:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 26, "metric_value": -0.0, "depth": 5}
               if obj[8]<=96:
                  # {"feature": "Total_Protiens", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[6]>62:
                     # {"feature": "Direct_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[2]>6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=61:
                           return 'normal'
                        elif obj[4]>61:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[6]<=62:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=80:
                           return 'liver'
                        elif obj[4]>80:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>96:
                  # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[6]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]>3:
                        return 'normal'
                     elif obj[2]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=6:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[8]<=69:
               # {"feature": "Total_Bilirubin", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[1]<=63.29032258064516:
                  # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[5]>36:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]>36:
                           return 'liver'
                        elif obj[4]<=36:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=36:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>8:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>63.29032258064516:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]>69:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 69, "metric_value": -0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Total_Protiens", "instances": 58, "metric_value": -0.0, "depth": 6}
                  if obj[6]>6.7280356841995825:
                     # {"feature": "Alamine_Aminotransferase", "instances": 53, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=44.75471698113208:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 39, "metric_value": 0.0, "depth": 8}
                        if obj[5]>12:
                           return 'liver'
                        elif obj[5]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>44.75471698113208:
                        # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[1]>2:
                           return 'liver'
                        elif obj[1]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=6.7280356841995825:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[5]>32:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]>9:
                        return 'liver'
                     elif obj[1]<=9:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'normal'
                        elif obj[4]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=32:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>52:
                           return 'liver'
                        elif obj[6]<=52:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=24:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=42:
                           return 'normal'
                        elif obj[5]>42:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>24:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=53:
                        return 'liver'
                     elif obj[5]>53:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=4:
                     return 'liver'
                  elif obj[1]>4:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": -0.0, "depth": 5}
               if obj[1]<=68.87878787878788:
                  # {"feature": "Total_Protiens", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=54:
                     return 'liver'
                  elif obj[6]>54:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=7:
                        return 'liver'
                     elif obj[8]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=67:
                           return 'liver'
                        elif obj[5]>67:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>68.87878787878788:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=88:
                     # {"feature": "Total_Protiens", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[6]>51:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[8]>4:
                           return 'normal'
                        elif obj[8]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=51:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>88:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[1]>5:
                  return 'liver'
               elif obj[1]<=5:
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
            # {"feature": "Total_Protiens", "instances": 116, "metric_value": -0.0, "depth": 4}
            if obj[6]<=84.16676164311447:
               # {"feature": "Aspartate_Aminotransferase", "instances": 109, "metric_value": -0.0, "depth": 5}
               if obj[5]<=135.61467889908258:
                  # {"feature": "Total_Bilirubin", "instances": 91, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=103.2001099722559:
                     # {"feature": "Direct_Bilirubin", "instances": 88, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=5:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 74, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'normal'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>5:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=54:
                           return 'liver'
                        elif obj[4]>54:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>103.2001099722559:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>135.61467889908258:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=179:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>179:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>84.16676164311447:
               # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 5}
               if obj[5]>19:
                  # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
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
            # {"feature": "Aspartate_Aminotransferase", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[5]<=178.28947368421052:
               # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[4]<=33:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=23:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[8]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>23:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>33:
                  # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Total_Protiens", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=68:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>68:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'liver'
                        elif obj[8]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>178.28947368421052:
               # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[6]<=69:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>152:
                        return 'liver'
                     elif obj[4]<=152:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]>9:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>69:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[6]>44.49473684210526:
            # {"feature": "Direct_Bilirubin", "instances": 63, "metric_value": -0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 55, "metric_value": -0.0, "depth": 5}
               if obj[8]<=8:
                  # {"feature": "Alkaline_Phosphotase", "instances": 32, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[1]>26:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>88:
                           return 'liver'
                        elif obj[5]<=88:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=26:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>37:
                           return 'normal'
                        elif obj[4]<=37:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>8:
                  # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 20, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=54:
                        # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>54:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
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
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Alkaline_Phosphotase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>20:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'normal'
                        elif obj[5]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=20:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[6]<=44.49473684210526:
            # {"feature": "Alkaline_Phosphotase", "instances": 32, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[8]<=13:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[5]>23:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=38:
                           return 'liver'
                        elif obj[4]>38:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>6:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=23:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=25:
                           return 'liver'
                        elif obj[4]>25:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>13:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[1]>9:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=10:
                           return 'normal'
                        elif obj[4]>10:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=3:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[5]>48:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
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
                  else:
                     return 'liver'
               elif obj[1]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=30:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
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
