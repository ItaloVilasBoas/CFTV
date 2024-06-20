import type { AxiosInstance, AxiosResponse } from 'axios'
import axios from 'axios'
import { Setor } from 'src/shared/types/setor.type';

const service: AxiosInstance = axios.create({
  baseURL: 'http://localhost/setor'
});

class SetorService {
  async getAll(): Promise<Setor[]> {
    const response: AxiosResponse<Setor[]> = await service.get('');
    return response.data;
  }

  async getById(id: number): Promise<Setor> {
    const response: AxiosResponse<Setor> = await service.get(`/${id}`);
    return response.data;
  }

  async create(setor: Setor): Promise<Setor> {
    const response: AxiosResponse<Setor> = await service.post('', setor);
    return response.data;
  }

  async update(setor: Setor): Promise<Setor> {
    const response: AxiosResponse<Setor> = await service.put(`/${setor.id}`, {
      nome: setor.nome,
      cameras: setor.cameras,
    });
    return response.data;
  }

  async delete(id: number): Promise<void> {
    const response: AxiosResponse<void> = await service.delete(`/${id}`);
    return response.data;
  }
}

export default new SetorService();

