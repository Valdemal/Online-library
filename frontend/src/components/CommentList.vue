<template>
  <div class="comments-layout">
    <div class="comments-label flex-center">Комментарии</div>
    <div class="comment">
      <div class="photo">
        <img src="../assets/Булгаков.jpg" alt="Булгаков">
        <EstimationWidget>
          <div>🌟4,5</div>
        </EstimationWidget>
      </div>
      <div class="text">
        <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio, dolor ex id iure odio
          suscipit vel. Alias eum harum ipsa modi natus, nulla porro, saepe totam vero voluptas,
          voluptatem voluptatum.
        </div>
        <div>Ad dolore incidunt nam nihil qui! Cumque, deserunt dignissimos earum eius esse eum explicabo
          incidunt inventore nam nihil non perferendis provident quidem quos reiciendis similique sint
          tempora tenetur unde velit.
        </div>
        <div>A, assumenda, incidunt. Aliquid aperiam architecto corporis eos exercitationem id ipsa ipsum
          natus sunt voluptates. A dolorem ducimus laboriosam nostrum voluptates? Cupiditate doloribus eum
          ex facilis libero quaerat quidem repudiandae?
        </div>
        <div>A aut enim fuga laudantium, molestiae quas quisquam repellendus. Ab alias at commodi
          consequuntur corporis distinctio dolores doloribus eius facere facilis laborum magni minus neque
          officia praesentium quasi, repellendus totam.
        </div>
        <div>Accusantium animi cum dolorem doloremque eum expedita inventore minima molestias omnis possimus
          quas quo, ratione rem saepe sed! Blanditiis, error eum expedita inventore itaque molestiae
          numquam provident qui sequi voluptatum!
        </div>
        <div>Alias assumenda blanditiis culpa deleniti doloremque earum error fugiat hic impedit ipsum iste
          nam nihil odit pariatur quam reiciendis, rem temporibus voluptatum. Aliquam debitis facilis fuga
          labore molestiae nam voluptatibus.
        </div>
        <div>Ad, amet atque, dolorem dolores ea eveniet exercitationem explicabo fugiat illum laboriosam
          magni maxime nihil nostrum obcaecati omnis perferendis placeat possimus quam quibusdam quidem
          reprehenderit, repudiandae tempora tempore vel veritatis.
        </div>
        <div>Accusantium alias corporis cumque distinctio ea eos eum ex expedita fugit hic ipsa iste
          laboriosam magni maiores natus officiis optio perferendis perspiciatis placeat possimus,
          praesentium repellat repellendus rerum. Consequatur, nulla.
        </div>
        <div>Accusamus animi cum deleniti laboriosam maiores odit officiis pariatur perspiciatis, possimus
          qui reiciendis tempore voluptatem voluptates! Consequuntur iste nisi obcaecati officia omnis
          porro sunt. A animi autem deleniti dolore perspiciatis.
        </div>
        <div>Deleniti, deserunt dignissimos fuga fugit ipsum magnam modi obcaecati officia repellat sit! At
          cum doloribus ea ex ipsa nesciunt pariatur, quaerat quibusdam? Consectetur, dolores magni quas
          qui quibusdam quo reiciendis.
        </div>
        <div>Adipisci beatae commodi eaque eos esse est ex excepturi iste minus, nemo odit quae, quam quod
          quos repudiandae sed sunt unde voluptas voluptates voluptatum. Beatae consectetur ea incidunt
          itaque quisquam.
        </div>
        <div>Error excepturi ipsa labore nobis rerum sed ullam. Alias aperiam cumque dolor eos expedita,
          fuga fugiat harum, illum odit optio quas reprehenderit, sed tempora velit vero voluptas
          voluptate! Debitis, sapiente.
        </div>
        <div>Cum est fugiat molestiae quibusdam sapiente! Aperiam, deserunt dolor ducimus ipsa iure
          reiciendis voluptatum. Incidunt odio quam velit. Adipisci amet doloremque doloribus eaque error
          excepturi labore numquam quia soluta sunt?
        </div>
        <div>Consequatur officia quo similique. A aliquam, explicabo. Cupiditate dicta eligendi facere fuga
          iste non praesentium rerum sunt veniam. Alias consequatur deleniti dolor dolore mollitia porro,
          quam quisquam quos sed veritatis?
        </div>
        <div>Alias autem deleniti dolorem doloribus enim eos et ex expedita fuga fugiat illum laudantium
          minus molestiae, non numquam perferendis, quaerat, quis repellat sapiente suscipit temporibus
          ullam velit voluptate! Nostrum, porro.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import EstimationWidget from '@/components/BaseEstimation.vue'
</script>

<style scoped>

.comments-label {
  background-color: #D9D9D9;
  font-size: 20px;
}

.comments-layout {
  margin-top: 10px;
}

.comment .photo {
  border-top: none;
  width: 110px;
  min-width: 110px;
}

.comment {
  display: flex;
  margin-top: 10px;
  border-top: 5px solid rgba(63, 159, 248, 0.7);
  max-height: 200px;
}

.comment .text {
  overflow: scroll;
  overflow-x: hidden;
}

</style>
