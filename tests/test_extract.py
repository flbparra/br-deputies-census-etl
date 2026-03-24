import pytest
import pandas as pd
import requests
from src.extract import extract_all, get_deputies_data, get_population_data

def test_extract_all_with_api_failure(mocker):
    """
    Testa se o pipeline lida corretamente com uma falha total de API (ex: timeout).
    Deve retornar DataFrames (mesmo que vazios ou mock) em vez de quebrar.
    """
    # Simula um erro de conexão em qualquer chamada do requests
    mocker.patch("requests.get", side_effect=requests.exceptions.ConnectionError("Erro de Rede UnB"))
    
    # O pipeline deve capturar a exceção e não travar
    df_despesas, df_populacao = extract_all()
    
    assert isinstance(df_despesas, pd.DataFrame)
    assert isinstance(df_populacao, pd.DataFrame)
    # Por enquanto, o stub retorna DF vazio no catch, mas futuramente testaremos o mock realista

def test_get_deputies_data_empty_response(mocker):
    """
    Testa o comportamento quando a API da Câmara retorna um status de erro (ex: 404).
    """
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch("requests.get", return_value=mock_response)
    
    # Atualmente o stub apenas loga e retorna vazio, vamos validar se retorna DataFrame
    df = get_deputies_data()
    assert isinstance(df, pd.DataFrame)

def test_extract_all_returns_dataframes():
    """
    Testa se a função principal sempre retorna dois objetos.
    """
    result = extract_all()
    assert len(result) == 2
    assert all(isinstance(x, pd.DataFrame) for x in result)
