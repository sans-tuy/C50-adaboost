def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Alamine_Aminotransferase", "instances": 520, "metric_value": 0.8591, "depth": 1}
   if obj[4]>10:
      # {"feature": "Age", "instances": 517, "metric_value": 0.8534, "depth": 2}
      if obj[0]>4:
         # {"feature": "Aspartate_Aminotransferase", "instances": 515, "metric_value": 0.8496, "depth": 3}
         if obj[5]>10:
            # {"feature": "Direct_Bilirubin", "instances": 514, "metric_value": 0.8476, "depth": 4}
            if obj[2]<=41.39736136789894:
               # {"feature": "Total_Bilirubin", "instances": 468, "metric_value": 0.8829, "depth": 5}
               if obj[1]<=16.185897435897434:
                  # {"feature": "Alkaline_Phosphotase", "instances": 335, "metric_value": 0.953, "depth": 6}
                  if obj[3]<=599.9631844541561:
                     # {"feature": "Albumin", "instances": 323, "metric_value": 0.9628, "depth": 7}
                     if obj[7]>1:
                        # {"feature": "Total_Protiens", "instances": 322, "metric_value": 0.9636, "depth": 8}
                        if obj[6]>5:
                           # {"feature": "Albumin_and_Globulin_Ratio", "instances": 316, "metric_value": 0.9663, "depth": 9}
                           if obj[8]>1:
                              return 'liver'
                           elif obj[8]<=1:
                              return 'liver'
                           else:
                              return 'liver'
                        elif obj[6]<=5:
                           # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[8]<=9:
                              return 'liver'
                           elif obj[8]>9:
                              return 'liver'
                           else:
                              return 'liver'
                        else:
                           return 'liver'
                     elif obj[7]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>599.9631844541561:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>16.185897435897434:
                  # {"feature": "Total_Protiens", "instances": 133, "metric_value": 0.5302, "depth": 6}
                  if obj[6]>30.585159171409632:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 110, "metric_value": 0.5983, "depth": 7}
                     if obj[8]<=75.24428872908071:
                        # {"feature": "Albumin", "instances": 103, "metric_value": 0.623, "depth": 8}
                        if obj[7]>2:
                           # {"feature": "Alkaline_Phosphotase", "instances": 100, "metric_value": 0.6343, "depth": 9}
                           if obj[3]<=1149.3957467619575:
                              return 'liver'
                           elif obj[3]>1149.3957467619575:
                              return 'normal'
                           else:
                              return 'normal'
                        elif obj[7]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>75.24428872908071:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=30.585159171409632:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>41.39736136789894:
               return 'liver'
            else:
               return 'liver'
         elif obj[5]<=10:
            return 'normal'
         else:
            return 'normal'
      elif obj[0]<=4:
         return 'normal'
      else:
         return 'normal'
   elif obj[4]<=10:
      return 'normal'
   else:
      return 'normal'
