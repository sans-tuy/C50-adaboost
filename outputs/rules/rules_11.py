def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 306, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 233, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 185, "metric_value": -0.0, "depth": 4}
            if obj[6]>13.159219399032203:
               # {"feature": "Direct_Bilirubin", "instances": 158, "metric_value": -0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Age", "instances": 140, "metric_value": 0.0, "depth": 6}
                  if obj[0]<=44.1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 71, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=137.91549295774647:
                        # {"feature": "Alamine_Aminotransferase", "instances": 59, "metric_value": -0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>137.91549295774647:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=59:
                           return 'liver'
                        elif obj[1]>59:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]>44.1:
                     # {"feature": "Total_Bilirubin", "instances": 69, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=13.608695652173912:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 52, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=40.40384615384615:
                           return 'liver'
                        elif obj[5]>40.40384615384615:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>13.608695652173912:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=7:
                     # {"feature": "Age", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[0]<=38:
                        # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=90:
                           return 'normal'
                        elif obj[4]>90:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[0]>38:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]>20:
                           return 'liver'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>7:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=13.159219399032203:
               # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 5}
               if obj[2]<=5:
                  # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]>33:
                           return 'liver'
                        elif obj[5]<=33:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>25:
                        # {"feature": "Age", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[0]<=63:
                           return 'liver'
                        elif obj[0]>63:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=25:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>5:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[1]>22:
                     return 'liver'
                  elif obj[1]<=22:
                     # {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[0]>35:
                        return 'liver'
                     elif obj[0]<=35:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Age", "instances": 48, "metric_value": 0.0, "depth": 4}
            if obj[0]<=57.44569923452688:
               # {"feature": "Total_Protiens", "instances": 39, "metric_value": -0.0, "depth": 5}
               if obj[6]>7:
                  # {"feature": "Direct_Bilirubin", "instances": 36, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=54:
                        # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[4]>14:
                           return 'liver'
                        elif obj[4]<=14:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>54:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[5]>19:
                           return 'liver'
                        elif obj[5]<=19:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>41:
                           return 'liver'
                        elif obj[4]<=41:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=7:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
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
            elif obj[0]>57.44569923452688:
               # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[1]<=8:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>16:
                           return 'liver'
                        elif obj[4]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=20:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>14:
                           return 'normal'
                        elif obj[4]<=14:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[2]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>8:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[3]>291.0539499036609:
         # {"feature": "Age", "instances": 73, "metric_value": 0.0, "depth": 3}
         if obj[0]>4:
            # {"feature": "Direct_Bilirubin", "instances": 72, "metric_value": 0.0, "depth": 4}
            if obj[2]<=117.15844405484265:
               # {"feature": "Aspartate_Aminotransferase", "instances": 69, "metric_value": -0.0, "depth": 5}
               if obj[5]<=133.2753623188406:
                  # {"feature": "Total_Protiens", "instances": 48, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=84.1003011150311:
                     # {"feature": "Alamine_Aminotransferase", "instances": 46, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=53.71739130434783:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 29, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=8:
                           return 'liver'
                        elif obj[8]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>53.71739130434783:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[8]>8:
                           return 'liver'
                        elif obj[8]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>84.1003011150311:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>133.2753623188406:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[2]>117.15844405484265:
               return 'liver'
            else:
               return 'liver'
         elif obj[0]<=4:
            return 'normal'
         else:
            return 'normal'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Age", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[0]<=46.051643192488264:
         # {"feature": "Alkaline_Phosphotase", "instances": 114, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 85, "metric_value": 0.0, "depth": 4}
            if obj[6]>21.097259464128964:
               # {"feature": "Alamine_Aminotransferase", "instances": 64, "metric_value": 0.0, "depth": 5}
               if obj[4]>11:
                  # {"feature": "Direct_Bilirubin", "instances": 63, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 52, "metric_value": -0.0, "depth": 7}
                     if obj[8]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[5]>13:
                           return 'liver'
                        elif obj[5]<=13:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=7:
                        # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=68:
                           return 'liver'
                        elif obj[1]>68:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[5]>20:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[8]>5:
                           return 'liver'
                        elif obj[8]<=5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=20:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=11:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=21.097259464128964:
               # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>1:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=32:
                           return 'normal'
                        elif obj[5]>32:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[2]>2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 29, "metric_value": 0.0, "depth": 4}
            if obj[8]>5:
               # {"feature": "Direct_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[2]<=32:
                  # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[1]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[5]>40:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=56:
                           return 'normal'
                        elif obj[6]>56:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=40:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>32:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=5:
               # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[1]>14:
                  # {"feature": "Total_Protiens", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[6]>61:
                     return 'liver'
                  elif obj[6]<=61:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[5]>48:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
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
               elif obj[1]<=14:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=34:
                     return 'normal'
                  elif obj[5]>34:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[0]>46.051643192488264:
         # {"feature": "Alkaline_Phosphotase", "instances": 99, "metric_value": -0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 66, "metric_value": -0.0, "depth": 4}
            if obj[8]<=11:
               # {"feature": "Total_Protiens", "instances": 55, "metric_value": -0.0, "depth": 5}
               if obj[6]>47.72727272727273:
                  # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": -0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=184:
                        # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=47.666666666666664:
                           return 'liver'
                        elif obj[4]>47.666666666666664:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>184:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=27:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'liver'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>27:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        elif obj[1]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=47.72727272727273:
                  # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[4]>24:
                     # {"feature": "Total_Bilirubin", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=58:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>58:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=24:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        return 'liver'
                     elif obj[1]<=7:
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
               else:
                  return 'liver'
            elif obj[8]>11:
               # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[6]<=51:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=4:
                        return 'liver'
                     elif obj[1]>4:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]>51:
                  # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": -0.0, "depth": 4}
            if obj[1]<=63.96969696969697:
               # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 5}
               if obj[4]>20:
                  # {"feature": "Total_Protiens", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[6]>47:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=6:
                        return 'liver'
                     elif obj[8]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>3:
                           return 'liver'
                        elif obj[2]<=3:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]<=47:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=20:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]>28:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'normal'
                     elif obj[2]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=28:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>63.96969696969697:
               # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 5}
               if obj[5]>29:
                  # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=76:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[4]>35:
                        # {"feature": "Total_Protiens", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[6]>7:
                           return 'liver'
                        elif obj[6]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=35:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>76:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=29:
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
