import pandas as pd


from sksurv.nonparametric import kaplan_meier_estimator


def calcular_kaplan_meier(df, col_duracion, col_estado_muerto):
    time, survival_prob, conf_init = kaplan_meier_estimator(
        df[col_estado_muerto], df[col_duracion], conf_type="log-log"
    )

    resultado = pd.DataFrame(
        {
            "tiempo": time,
            "probabilidad_sobrevivencia": survival_prob,
            "limite_confianza_bajo": conf_init[0],
            "limite_confianza_alto": conf_init[1],
        }
    )
    return resultado
