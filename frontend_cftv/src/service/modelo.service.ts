import type { AxiosInstance, AxiosResponse } from 'axios'
import axios from 'axios'

const service: AxiosInstance = axios.create({
  baseURL: 'http://localhost/treinar_modelo'
});

class TreinarModeloService {
  async treinarModelo(): Promise<void> {
    const response: AxiosResponse<void> = await service.get('');
    return response.data;
  }
}

export default new TreinarModeloService();

