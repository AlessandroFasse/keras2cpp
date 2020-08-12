#include "keras2cpp/layers/locally2d.h"
namespace keras2cpp{
    namespace layers{
        LocallyConnected2D::LocallyConnected2D(Stream& file)
        : weights_(file, 4), biases_(file, 3), activation_(file) {}

        Tensor LocallyConnected2D::operator()(const Tensor& in) const noexcept {
            return activation_(in);
        }
    }
}
