import numpy as np
import time


def mult_basic(N, M, L, a, x, y):
    """ �s��v�Z�͎g�킸��For���[�v�Ōv�Z����֐�
        �������A���]�̃T�C�Y�̔�ndarray���쐬����̂�����Ȃ̂ŁA
        ���͂̕ϐ���NumPy��ndarray�Ƃ��Đ������ēn�� """
    r = np.empty((N, L))
    for i in range(N):
        for j in range(L):
            tmp = 0.0
            for k in range(M):
                tmp = tmp + a[k]*x[i][k]*y[k][j]
            r[i][j] = tmp
    return r


def mult_fast(N, M, L, a, x, y):
    """ NumPy�̊֐����g���č����Ɍv�Z����֐�
        �֐�mult_basic�ƑS���������ʂ𓾂�"""
    return np.dot(x*a, y)  # �����̋L�q�͂�������1�s


if __name__ == '__main__':
    # �v�Z�Ɏg���z��̐���
    np.random.seed(0)
    N = 10000
    M = 1000
    L = 10000
    a = np.random.random(M) - 0.5
    x = np.random.random((N, M)) - 0.5
    y = np.random.random((M, L)) - 0.5

    # �s��v�Z�͎g�킸��For���[�v�Ōv�Z
    ts = time.time()
    r1 = mult_basic(N, M, L, a, x, y)
    te = time.time()
    print("Basic method : %.3f [ms]" % (1000*(te - ts)))

    # NumPy�̊֐����g���č����ɏ���
    ts = time.time()
    r2 = mult_fast(N, M, L, a, x, y)
    te = time.time()
    print("Fast method  : %.3f [ms]" % (1000*(te - ts)))

