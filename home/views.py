from django.shortcuts import render
import pandas as pd
import joblib

def home(request, *args, **kwargs):
    context = {
        'home': home,
    }

    return render(
        request,
        'home/index.html',
        context=context
    )

def whatsapp(request, *args, **kwargs):
    context = {
        'whatsapp': whatsapp,
    }

    return render(
        request,
        'home/n8n.html',
        context=context
    )


COLUNAS_MODELO = ['months_as_customer', 'age', 'policy_deductable', 'policy_annual_premium', 'umbrella_limit', 'insured_zip', 'capital-gains', 'capital-loss', 'incident_hour_of_the_day', 'number_of_vehicles_involved', 'bodily_injuries', 'witnesses', 'total_claim_amount', 'injury_claim', 'property_claim', 'vehicle_claim', 'auto_year', 'policy_state_IN', 'policy_state_OH', 'policy_csl_250/500', 'policy_csl_500/1000', 'insured_sex_MALE', 'insured_education_level_College', 'insured_education_level_High School', 'insured_education_level_JD', 'insured_education_level_MD', 'insured_education_level_Masters', 'insured_education_level_PhD', 'insured_occupation_armed-forces', 'insured_occupation_craft-repair', 'insured_occupation_exec-managerial', 'insured_occupation_farming-fishing', 'insured_occupation_handlers-cleaners', 'insured_occupation_machine-op-inspct', 'insured_occupation_other-service', 'insured_occupation_priv-house-serv', 'insured_occupation_prof-specialty', 'insured_occupation_protective-serv', 'insured_occupation_sales', 'insured_occupation_tech-support', 'insured_occupation_transport-moving', 'insured_hobbies_basketball', 'insured_hobbies_board-games', 'insured_hobbies_bungie-jumping', 'insured_hobbies_camping', 'insured_hobbies_chess', 'insured_hobbies_cross-fit', 'insured_hobbies_dancing', 'insured_hobbies_exercise', 'insured_hobbies_golf', 'insured_hobbies_hiking', 'insured_hobbies_kayaking', 'insured_hobbies_movies', 'insured_hobbies_paintball', 'insured_hobbies_polo', 'insured_hobbies_reading', 'insured_hobbies_skydiving', 'insured_hobbies_sleeping', 'insured_hobbies_video-games', 'insured_hobbies_yachting', 'insured_relationship_not-in-family', 'insured_relationship_other-relative', 'insured_relationship_own-child', 'insured_relationship_unmarried', 'insured_relationship_wife', 'incident_date_2015-01-02', 'incident_date_2015-01-03', 'incident_date_2015-01-04', 'incident_date_2015-01-05', 'incident_date_2015-01-06', 'incident_date_2015-01-07', 'incident_date_2015-01-08', 'incident_date_2015-01-09', 'incident_date_2015-01-10', 'incident_date_2015-01-11', 'incident_date_2015-01-12', 'incident_date_2015-01-13', 'incident_date_2015-01-14', 'incident_date_2015-01-15', 'incident_date_2015-01-16', 'incident_date_2015-01-17', 'incident_date_2015-01-18', 'incident_date_2015-01-19', 'incident_date_2015-01-20', 'incident_date_2015-01-21', 'incident_date_2015-01-22', 'incident_date_2015-01-23', 'incident_date_2015-01-24', 'incident_date_2015-01-25', 'incident_date_2015-01-26', 'incident_date_2015-01-27', 'incident_date_2015-01-28', 'incident_date_2015-01-29', 'incident_date_2015-01-30', 'incident_date_2015-01-31', 'incident_date_2015-02-01', 'incident_date_2015-02-02', 'incident_date_2015-02-03', 'incident_date_2015-02-04', 'incident_date_2015-02-05', 'incident_date_2015-02-06', 'incident_date_2015-02-07', 'incident_date_2015-02-08', 'incident_date_2015-02-09', 'incident_date_2015-02-10', 'incident_date_2015-02-11', 'incident_date_2015-02-12', 'incident_date_2015-02-13', 'incident_date_2015-02-14', 'incident_date_2015-02-15', 'incident_date_2015-02-16', 'incident_date_2015-02-17', 'incident_date_2015-02-18', 'incident_date_2015-02-19', 'incident_date_2015-02-20', 'incident_date_2015-02-21', 'incident_date_2015-02-22', 'incident_date_2015-02-23', 'incident_date_2015-02-24', 'incident_date_2015-02-25', 'incident_date_2015-02-26', 'incident_date_2015-02-27', 'incident_date_2015-02-28', 'incident_date_2015-03-01', 'incident_type_Parked Car', 'incident_type_Single Vehicle Collision', 'incident_type_Vehicle Theft', 'collision_type_Rear Collision', 'collision_type_Side Collision', 'incident_severity_Minor Damage', 'incident_severity_Total Loss', 'incident_severity_Trivial Damage', 'authorities_contacted_Fire', 'authorities_contacted_Other', 'authorities_contacted_Police', 'incident_state_NY', 'incident_state_OH', 'incident_state_PA', 'incident_state_SC', 'incident_state_VA', 'incident_state_WV', 'incident_city_Columbus', 'incident_city_Hillsdale', 'incident_city_Northbend', 'incident_city_Northbrook', 'incident_city_Riverwood', 'incident_city_Springfield', 'property_damage_YES', 'police_report_available_YES', 'auto_make_Audi', 'auto_make_BMW', 'auto_make_Chevrolet', 'auto_make_Dodge', 'auto_make_Ford', 'auto_make_Honda', 'auto_make_Jeep', 'auto_make_Mercedes', 'auto_make_Nissan', 'auto_make_Saab', 'auto_make_Suburu', 'auto_make_Toyota', 'auto_make_Volkswagen', 'auto_model_92x', 'auto_model_93', 'auto_model_95', 'auto_model_A3', 'auto_model_A5', 'auto_model_Accord', 'auto_model_C300', 'auto_model_CRV', 'auto_model_Camry', 'auto_model_Civic', 'auto_model_Corolla', 'auto_model_E400', 'auto_model_Escape', 'auto_model_F150', 'auto_model_Forrestor', 'auto_model_Fusion', 'auto_model_Grand Cherokee', 'auto_model_Highlander', 'auto_model_Impreza', 'auto_model_Jetta', 'auto_model_Legacy', 'auto_model_M5', 'auto_model_MDX', 'auto_model_ML350', 'auto_model_Malibu', 'auto_model_Maxima', 'auto_model_Neon', 'auto_model_Passat', 'auto_model_Pathfinder', 'auto_model_RAM', 'auto_model_RSX', 'auto_model_Silverado', 'auto_model_TL', 'auto_model_Tahoe', 'auto_model_Ultima', 'auto_model_Wrangler', 'auto_model_X5','auto_model_X6']

def seguro(request):
    if request.method == 'POST':
        try:
            modelo = joblib.load('modelo_fraude_rf.joblib')

            df_para_prever = pd.DataFrame(0, index=[0], columns=COLUNAS_MODELO)

            df_para_prever['months_as_customer'] = int(request.POST.get('months_as_customer'))
            df_para_prever['age'] = int(request.POST.get('age'))
            df_para_prever['total_claim_amount'] = float(request.POST.get('total_claim_amount'))
            df_para_prever['witnesses'] = int(request.POST.get('witnesses'))
            df_para_prever['auto_year'] = int(request.POST.get('auto_year'))

            severity = request.POST.get('incident_severity')
            coluna_severity = f'incident_severity_{severity}'
            if coluna_severity in df_para_prever.columns:
                df_para_prever[coluna_severity] = 1

            auto_make = request.POST.get('auto_make')
            coluna_auto_make = f'auto_make_{auto_make}'
            if coluna_auto_make in df_para_prever.columns:
                df_para_prever[coluna_auto_make] = 1

            police_report = request.POST.get('police_report_available')
            if police_report == 'YES':
                df_para_prever['police_report_available_YES'] = 1
            
            probabilidade_fraude = modelo.predict_proba(df_para_prever[COLUNAS_MODELO])[0][1]
            resultado = round(probabilidade_fraude * 100, 2)

            context = {'probabilidade': resultado}
            return render(request, 'home/seguro_resultado.html', context)

        except Exception as e:
            return render(request, 'home/seguro.html', {'erro': f"Ocorreu um erro: {e}"})

    return render(request, 'home/seguro.html')


def credito(request):
    context = {}
    
    if request.method == 'POST':
        modelo = joblib.load('modelo_risco_credito.joblib')

        form_data = {
            'status_conta_corrente': request.POST.get('status_conta_corrente'),
            'duracao_mes': int(request.POST.get('duracao_mes')),
            'historico_credito': request.POST.get('historico_credito'),
            'proposito': request.POST.get('proposito'),
            'valor_credito': int(request.POST.get('valor_credito')),
            'poupanca': request.POST.get('poupanca'),
            'emprego_atual': request.POST.get('emprego_atual'),
            'taxa_instalment': int(request.POST.get('taxa_instalment')),
            'estado_civil_sexo': request.POST.get('estado_civil_sexo'),
            'outros_devedores': request.POST.get('outros_devedores'),
            'residencia_atual_desde': int(request.POST.get('residencia_atual_desde')),
            'propriedade': request.POST.get('propriedade'),
            'idade': int(request.POST.get('idade')),
            'outros_planos_pagamento': request.POST.get('outros_planos_pagamento'),
            'moradia': request.POST.get('moradia'),
            'n_creditos_existentes': int(request.POST.get('n_creditos_existentes')),
            'emprego': request.POST.get('emprego'),
            'n_dependentes': int(request.POST.get('n_dependentes')),
            'telefone': request.POST.get('telefone'),
            'trabalhador_estrangeiro': request.POST.get('trabalhador_estrangeiro'),
        }

        colunas_modelo = [
            'duracao_mes', 'valor_credito', 'taxa_instalment', 'residencia_atual_desde', 'idade',
            'n_creditos_existentes', 'n_dependentes', 'status_conta_corrente_A11', 'status_conta_corrente_A12',
            'status_conta_corrente_A13', 'status_conta_corrente_A14', 'historico_credito_A30', 'historico_credito_A31',
            'historico_credito_A32', 'historico_credito_A33', 'historico_credito_A34', 'proposito_A40',
            'proposito_A41', 'proposito_A410', 'proposito_A42', 'proposito_A43', 'proposito_A44',
            'proposito_A45', 'proposito_A46', 'proposito_A48', 'proposito_A49', 'poupanca_A61', 'poupanca_A62',
            'poupanca_A63', 'poupanca_A64', 'poupanca_A65', 'emprego_atual_A71', 'emprego_atual_A72',
            'emprego_atual_A73', 'emprego_atual_A74', 'emprego_atual_A75', 'estado_civil_sexo_A91',
            'estado_civil_sexo_A92', 'estado_civil_sexo_A93', 'estado_civil_sexo_A94', 'outros_devedores_A101',
            'outros_devedores_A102', 'outros_devedores_A103', 'propriedade_A121', 'propriedade_A122',
            'propriedade_A123', 'propriedade_A124', 'outros_planos_pagamento_A141', 'outros_planos_pagamento_A142',
            'outros_planos_pagamento_A143', 'moradia_A151', 'moradia_A152', 'moradia_A153', 'emprego_A171',
            'emprego_A172', 'emprego_A173', 'emprego_A174', 'telefone_A191', 'telefone_A192',
            'trabalhador_estrangeiro_A201', 'trabalhador_estrangeiro_A202'
        ]

        dados_cliente = pd.DataFrame(0, index=[0], columns=colunas_modelo)

        for col in ['duracao_mes',
                    'valor_credito',
                    'taxa_instalment',
                    'residencia_atual_desde',
                    'idade', 'n_creditos_existentes',
                    'n_dependentes']:
            
            if col in form_data:
                dados_cliente[col] = form_data[col]
        
        for col_name, value in form_data.items():
            if isinstance(value, str):
                coluna_encoded = f'{col_name}_{value}'
                if coluna_encoded in dados_cliente.columns:
                    dados_cliente[coluna_encoded] = 1

        previsao = modelo.predict(dados_cliente)
        
        if previsao[0] == 0:
            resultado = "Crédito Aprovado! (Baixo Risco)"
        else:
            resultado = "Crédito Negado! (Alto Risco)"
        
        context['resultado'] = resultado
        
        context['form_data'] = form_data

    return render(request, 'home/analise_credito.html', context)