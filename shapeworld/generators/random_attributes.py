from random import random
from shapeworld.world import Entity
from shapeworld.generators import GenericGenerator


class RandomAttributesGenerator(GenericGenerator):

    def __init__(
        self,
        world_size=64,
        world_color='black',
        shapes=None,
        colors=None,
        textures=None,
        rotation=True,
        size_range=(0.1, 0.25),
        distortion_range=(2.0, 3.0),
        shade_range=0.4,
        collision_tolerance=0.25,
        collision_shade_difference=0.5,
        boundary_tolerance=0.25,
        entity_counts=(1,),
        train_entity_counts=None,
        validation_entity_counts=None,
        test_entity_counts=None,
        validation_combinations=None,
        test_combinations=None,
        max_provoke_collision_rate=0.33
    ):
        super(RandomAttributesGenerator, self).__init__(
            world_size=world_size,
            world_color=world_color,
            shapes=shapes,
            colors=colors,
            textures=textures,
            rotation=rotation,
            size_range=size_range,
            distortion_range=distortion_range,
            shade_range=shade_range,
            collision_tolerance=collision_tolerance,
            collision_shade_difference=collision_shade_difference,
            boundary_tolerance=boundary_tolerance,
            entity_counts=entity_counts,
            train_entity_counts=train_entity_counts,
            validation_entity_counts=validation_entity_counts,
            test_entity_counts=test_entity_counts,
            validation_combinations=validation_combinations,
            test_combinations=test_combinations
        )

        assert isinstance(max_provoke_collision_rate, float) and 0.0 <= max_provoke_collision_rate <= 1.0
        self.max_provoke_collision_rate = max_provoke_collision_rate

    def initialize(self, mode):
        super(RandomAttributesGenerator, self).initialize(mode=mode)
        self.provoke_collision_rate = random() * self.max_provoke_collision_rate

    def sample_entity(self, world, last_entity, combinations=None):
        if last_entity == -1:
            self.provoke_collision = random() < self.provoke_collision_rate
        elif last_entity is not None:
            self.provoke_collision = random() < self.provoke_collision_rate
        center = world.random_location(provoke_collision=self.provoke_collision)
        if combinations is None:
            return Entity.random_instance(center=center, rotation=self.rotation, size_range=self.size_range, distortion_range=self.distortion_range, shade_range=self.shade_range, shapes=self.shapes, colors=self.colors, textures=self.textures)
        else:
            return Entity.random_instance(center=center, rotation=self.rotation, size_range=self.size_range, distortion_range=self.distortion_range, shade_range=self.shade_range, combinations=combinations)