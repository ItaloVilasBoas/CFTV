import type { AxiosInstance, AxiosResponse } from 'axios'
import axios from 'axios'
import { Funcionario } from 'src/shared/types/funcionario.type';

const service: AxiosInstance = axios.create({
  baseURL: 'http://localhost/funcionario'
});

class FuncionarioService {
  async getAll(): Promise<Funcionario[]> {
    const response: AxiosResponse<Funcionario[]> = await service.get('');
    return response.data;
  }

  async getById(id: number): Promise<Funcionario> {
    const response: AxiosResponse<Funcionario> = await service.get(`/${id}`);
    return response.data;
  }

  async create(funcionario: Funcionario): Promise<Funcionario> {
    const response: AxiosResponse<Funcionario> = await service.post('', {
      nome: funcionario.nome,
      setores: funcionario.setores,
    });
    return response.data;
  }

  async update(funcionario: Funcionario): Promise<void> {
    const response: AxiosResponse<void> = await service.put(`/${funcionario.id}`, {
      nome: funcionario.nome,
      setores: funcionario.setores,
    });
    return response.data;
  }

  async updateFoto(id: number): Promise<void> {
    const response: AxiosResponse<void> = await service.put(`/${id}/foto`);
    return response.data;
  }

  async delete(id: number): Promise<void> {
    const response: AxiosResponse<void> = await service.delete(`/${id}`);
    return response.data;
  }
}

export default new FuncionarioService();

